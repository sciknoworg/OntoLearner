# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Fine-tuning for the Semantic-Swingers Task A learner — the training counterpart of inference.

The competition champion is a **LoRA fine-tune** of ``Qwen/Qwen3.5-9B``. Until now the fork shipped
only inference: ``fit()`` built the retrieval index and the adapter arrived pre-trained. This module
adds the code that *produces* the adapter, in two flavours that reconcile behind one interface:

* ``train_backend="peft"`` — transformers + PEFT LoRA SFT (the reported bf16/8-bit champions).
  Needs a CUDA GPU; the ``qwen3_5`` hybrid's fast-attention kernels do not exist on Apple Silicon.
* ``train_backend="mlx"`` — ``mlx_lm.lora`` on ``mlx-community/Qwen3.5-9B-4bit``. Runs on Apple
  Silicon; produces a *separate 4-bit artifact*, so its scores are not the bf16 champion numbers.

Two training regimes, matching the inference ``top_k``:

* ``train_mode="raft"`` — retrieval-aware: top-k exemplars are baked into each training prompt with
  **leave-one-out** retrieval (a doc never sees its own gold). Pairs with ``top_k > 0`` at inference.
* ``train_mode="baseft"`` — no exemplars in the prompt (k=0). Pairs with ``top_k = 0`` at inference.

The data-building and prompt-masking below are **pure Python** and unit-testable with no GPU and no
model download; only the two ``_train_*`` backends import the heavy stack, lazily, at call time.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple


@dataclass
class TrainConfig:
    """Hyper-parameters for a LoRA SFT run. Defaults mirror the team's champion runs."""

    output_dir: str
    base_model_id: str = "Qwen/Qwen3.5-9B"
    train_mode: str = "raft"                 # "raft" | "baseft"
    top_k: int = 10                          # exemplars baked into each prompt (raft only)
    seq_len: int = 3584                      # raft prompts are long; baseft can use 1024
    lora_r: int = 16
    lora_alpha: int = 32
    lora_dropout: float = 0.05
    learning_rate: float = 1e-5
    target_steps: int = 2000
    batch_size: int = 1
    grad_accum: int = 4
    save_every: int = 50
    steps_per_report: int = 25
    seed: int = 42
    # PEFT hybrid-arch LoRA targets (dense + linear-attention projections). Mirrors the team's
    # ft_nvidia.py default; the reported adapters were trained on exactly these modules.
    target_modules: Sequence[str] = field(default_factory=lambda: [
        "q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj",
        "in_proj_qkvz", "in_proj_ba",
    ])


# ---- data building (pure python, unit-testable) ------------------------------------------------


def build_training_pairs(
    train_docs: List[Dict[str, Any]],
    build_prompt: Callable[[str, List[Dict[str, Any]]], str],
    retrieve_exemplars: Callable[[str, str], List[Dict[str, Any]]],
    train_mode: str,
) -> List[Dict[str, str]]:
    """Turn ``[{doc_id, text, triples}]`` into ``[{prompt, completion}]`` SFT pairs.

    * ``build_prompt(text, exemplars)`` is the learner's own prompt builder, so training prompts are
      byte-identical to what inference sends — the single most important correctness property here.
    * ``retrieve_exemplars(text, exclude_id)`` must exclude the document's own id (**leave-one-out**)
      so a training doc never sees its own gold. For ``baseft`` we pass no exemplars at all.
    * ``completion`` is the gold triples as ``{"triples": [[s, r, o], ...]}`` — the exact surface
      form the inference parser expects, so we teach the model to emit what we later read back.
    """
    pairs: List[Dict[str, str]] = []
    for d in train_docs:
        text = d["text"]
        if train_mode == "raft":
            exemplars = retrieve_exemplars(text, d.get("doc_id", ""))   # leave-one-out
        else:
            exemplars = []
        prompt = build_prompt(text, exemplars)
        completion = json.dumps(
            {"triples": [list(t) for t in (d.get("triples") or [])]}, ensure_ascii=False
        )
        pairs.append({"prompt": prompt, "completion": completion})
    return pairs


def encode_example(
    tokenize_fn: Callable[[str], List[int]],
    eos_id: Optional[int],
    prompt: str,
    completion: str,
    max_len: int,
) -> Tuple[List[int], List[int]]:
    """Tokenize prompt+completion, **masking prompt tokens** (label ``-100``).

    Loss is computed only on completion tokens — the same ``--mask-prompt`` semantics ``mlx_lm``
    uses. Without this the model trains to reproduce the *document*, not to extract triples. On
    overflow, truncate from the LEFT of the prompt so the assistant-turn suffix and the full
    completion (the target) survive.
    """
    prompt_ids = list(tokenize_fn(prompt))
    completion_ids = list(tokenize_fn(completion))
    if eos_id is not None:
        completion_ids = completion_ids + [eos_id]
    if len(prompt_ids) + len(completion_ids) > max_len:
        keep = max(0, max_len - len(completion_ids))
        prompt_ids = prompt_ids[-keep:] if keep > 0 else []
    input_ids = prompt_ids + completion_ids
    labels = [-100] * len(prompt_ids) + completion_ids
    return input_ids[:max_len], labels[:max_len]


def write_jsonl(pairs: List[Dict[str, str]], path: Path) -> Path:
    """Persist SFT pairs; both backends read this file, and it is a useful artefact on its own."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for p in pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    return path


# ---- backend dispatch --------------------------------------------------------------------------


def train_adapter(pairs: List[Dict[str, str]], cfg: TrainConfig, backend: str) -> str:
    """Train a LoRA adapter from SFT pairs and return the path to the finished adapter dir.

    Dispatches to the CUDA (``peft``) or Apple-Silicon (``mlx``) backend. The heavy imports live
    inside each backend so this module imports cleanly with neither stack installed.
    """
    out = Path(cfg.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    write_jsonl(pairs, out / "train.jsonl")
    if backend == "peft":
        return _train_peft(pairs, cfg)
    if backend == "mlx":
        return _train_mlx(pairs, cfg)
    raise ValueError(f"train_backend must be 'peft' or 'mlx', got {backend!r}")


def _pad_batch(examples: Sequence[Tuple[List[int], List[int]]], pad_id: int) -> Dict[str, list]:
    max_len = max((len(ids) for ids, _ in examples), default=0)
    input_ids, attn, labels = [], [], []
    for ids, labs in examples:
        pad_n = max_len - len(ids)
        input_ids.append(ids + [pad_id] * pad_n)
        attn.append([1] * len(ids) + [0] * pad_n)
        labels.append(labs + [-100] * pad_n)
    return {"input_ids": input_ids, "attention_mask": attn, "labels": labels}


def _train_peft(pairs: List[Dict[str, str]], cfg: TrainConfig) -> str:
    """transformers + PEFT LoRA SFT with prompt masking. CUDA-only in practice.

    Ported from the team's ``data/ft/_runners/ft_nvidia.py`` — a manual loop (not ``Trainer``) so
    prompt masking and non-finite-loss skipping stay explicit and inspectable.
    """
    try:
        import random

        import torch
        from peft import LoraConfig, get_peft_model
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as e:
        raise RuntimeError(
            "train_backend='peft' needs torch + transformers + peft (a CUDA GPU in practice; the "
            "qwen3_5 kernels fall back to CPU on Apple Silicon). Install them on a GPU box, or use "
            "train_backend='mlx' on Apple Silicon. Original error: " + str(e)
        ) from e

    torch.manual_seed(cfg.seed)
    tok = AutoTokenizer.from_pretrained(cfg.base_model_id, trust_remote_code=True)
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        cfg.base_model_id, torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto"
    )
    model = get_peft_model(model, LoraConfig(
        r=cfg.lora_r, lora_alpha=cfg.lora_alpha, lora_dropout=cfg.lora_dropout,
        target_modules=list(cfg.target_modules), task_type="CAUSAL_LM", bias="none",
    ))

    def tokenize_fn(t: str) -> List[int]:
        return tok(t, add_special_tokens=False)["input_ids"]

    encoded = [encode_example(tokenize_fn, tok.eos_token_id, p["prompt"], p["completion"], cfg.seq_len)
               for p in pairs]
    device = next(model.parameters()).device
    optim = torch.optim.AdamW((p for p in model.parameters() if p.requires_grad), lr=cfg.learning_rate)
    model.train()
    rng = random.Random(cfg.seed)
    step = micro = 0
    optim.zero_grad()
    while step < cfg.target_steps:
        batch = _pad_batch([encoded[rng.randrange(len(encoded))] for _ in range(cfg.batch_size)],
                           tok.pad_token_id)
        out = model(input_ids=torch.tensor(batch["input_ids"], device=device),
                    attention_mask=torch.tensor(batch["attention_mask"], device=device),
                    labels=torch.tensor(batch["labels"], device=device))
        if not torch.isfinite(out.loss):
            optim.zero_grad(); micro += 1; continue
        (out.loss / cfg.grad_accum).backward()
        micro += 1
        if micro % cfg.grad_accum:
            continue
        torch.nn.utils.clip_grad_norm_((p for p in model.parameters() if p.requires_grad), 1.0)
        optim.step(); optim.zero_grad(); step += 1
        if step % cfg.steps_per_report == 0:
            print(f"[peft] step {step}/{cfg.target_steps} loss={out.loss.item():.4f}", flush=True)
        if step % cfg.save_every == 0:
            model.save_pretrained(Path(cfg.output_dir) / f"checkpoint-{step}")
    final = Path(cfg.output_dir) / "final"
    model.save_pretrained(final)
    return str(final)


def _train_mlx(pairs: List[Dict[str, str]], cfg: TrainConfig) -> str:
    """LoRA SFT via the ``mlx_lm lora`` **CLI** on Apple Silicon.

    Invokes ``python -m mlx_lm lora --train`` — the stable, version-robust entry point, and the exact
    command the team's own ``ft35_overnight.py`` used to produce the real MLX adapters. We do **not**
    bind ``mlx_lm``'s low-level ``tuner`` API: it churns across releases (the dataset ``__getitem__``
    contract and the LoRA-config keys have both shifted), so re-implementing the loop is fragile for
    no benefit. The CLI reads ``{prompt, completion}`` jsonl, applies prompt masking itself, and writes
    ``adapters.safetensors`` + ``adapter_config.json`` — the format ``backend="mlx"`` inference loads.

    The base defaults to the 4-bit MLX build, so the adapter is a *separate 4-bit artifact* from the
    bf16 PEFT champions (a Mac-native FT variant, not a reproduction of the reported scores).
    """
    import subprocess
    import sys

    out = Path(cfg.output_dir)
    write_jsonl(pairs, out / "train.jsonl")
    write_jsonl(pairs[: max(1, len(pairs) // 10)], out / "valid.jsonl")

    base = cfg.base_model_id
    if base == "Qwen/Qwen3.5-9B":                 # bf16 id -> its MLX-quantized sibling
        base = "mlx-community/Qwen3.5-9B-4bit"

    cmd = [
        sys.executable, "-m", "mlx_lm", "lora",
        "--model", base,
        "--train",
        "--data", str(out),
        "--fine-tune-type", "lora",
        "--num-layers", "8",
        "--batch-size", str(cfg.batch_size),
        "--iters", str(cfg.target_steps),
        "--max-seq-length", str(cfg.seq_len),
        "--learning-rate", str(cfg.learning_rate),
        "--steps-per-report", str(cfg.steps_per_report),
        "--save-every", str(cfg.save_every),
        "--adapter-path", str(out),
        "--grad-checkpoint",
    ]
    result = subprocess.run(cmd)
    if result.returncode != 0:
        raise RuntimeError(
            f"`mlx_lm lora` training failed (exit {result.returncode}). Command:\n  "
            + " ".join(cmd)
        )
    return str(out)
