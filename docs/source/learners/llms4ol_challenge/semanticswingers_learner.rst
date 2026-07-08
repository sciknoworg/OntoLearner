Semantic-Swingers Learner
==========================


.. sidebar:: Semantic-Swingers Learner Examples

   * Term Typing: `llm_learner_semanticswingers_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_semanticswingers_term_typing.py>`_
   * Taxonomy Discovery: `llm_learner_semanticswingers_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_semanticswingers_taxonomy_discovery.py>`_

The Semantic-Swingers team participated in the LLMs4OL 2026 Shared Task. This page documents
the term-typing learner (Task B) and the taxonomy-discovery learner (Task C). Both share the
same design: a strong sentence-embedding encoder plus a swappable selection step with three
interchangeable backends — an offline embedding heuristic (default, no API key), the OpenAI
competition champion, and a free local Ollama reproduction of the champion pipeline.

Term Typing (Task B)
---------------------------------

Closed-vocabulary term typing: ``fit`` learns the inventory of allowed type labels from the
train split, and at inference the selector assigns types to each term from that inventory only.

- ``"embedding"`` (default) — each term gets its nearest type label by sentence-embedding
  cosine similarity. Fully offline and deterministic.
- ``"openai"`` — the champion. An OpenAI chat model (default ``gpt-4.1-mini``) classifies
  term batches against the closed vocabulary with a precision-biased prompt (multi-type
  allowed, abstains when nothing fits, labels copied exactly).
- ``"ollama"`` — the same classification prompt served by a local Ollama model (default
  ``llama3.1:8b``). No API key required.

.. code-block:: python

   from ontolearner import Wine, train_test_split, LearnerPipeline
   from ontolearner.learner.term_typing import SemanticSwingersTermTypingLearner

   ontology = Wine()
   ontology.load()
   train_data, test_data = train_test_split(ontology.extract(), test_size=0.2, random_state=42)

   learner = SemanticSwingersTermTypingLearner(selector="embedding", device="cpu")

   pipeline = LearnerPipeline(llm=learner, llm_id="semanticswingers-term-typing")
   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       task="term-typing",
       evaluate=True,
   )
   print(outputs["metrics"])

Taxonomy Discovery (Task C)
---------------------------------

The learner treats taxonomy discovery as *retrieve-then-select*:

1. **Retrieve** — a sentence-embedding encoder embeds the type vocabulary; for every child
   type, the ``top_k`` nearest neighbours become candidate parents. The team's finding is
   that the *encoder* is the main lever for this stage, so the default encoder is
   ``mixedbread-ai/mxbai-embed-large-v1``.
2. **Select** — a selection step picks the parent for each child from its candidates.
   Three selectors are provided:

   - ``"embedding"`` (default) — fully offline and deterministic. The most *general*
     candidate (highest mean similarity to the whole vocabulary) is chosen as parent.
     No API key or LLM required; intended as a fast, reproducible baseline.
   - ``"openai"`` — the competition champion. An OpenAI chat model (default
     ``gpt-4.1-mini``) picks the parent from the retrieved candidates. Requires an
     API key (via the ``api_key`` argument or the ``OPENAI_API_KEY`` environment
     variable — never hard-coded); without a key the learner silently degrades to
     the embedding selector.
   - ``"ollama"`` — a free, local reproduction of the champion *pipeline*. The same
     selection prompt is served by a local `Ollama <https://ollama.com>`_ model
     (default ``llama3.1:8b``) through its OpenAI-compatible endpoint. No API key
     required. Prefer direct-answering models here: thinking models (e.g. Qwen3.5)
     spend their completion budget on reasoning tokens and need ``max_tokens=1024``
     or more to produce an answer at all.

The learner requires no training: ``fit`` is a no-op and all edges are induced at
inference time, so it works on unseen ontologies without any target-vocabulary
assumptions.

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import Wine, train_test_split

   ontology = Wine()
   ontology.load()
   data = ontology.extract()

   train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

Initialize Learner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner.learner.taxonomy_discovery import SemanticSwingersTaxonomyLearner

   # Offline baseline (no API key, deterministic)
   learner = SemanticSwingersTaxonomyLearner(
       embedding_model="mixedbread-ai/mxbai-embed-large-v1",
       top_k=30,
       selector="embedding",
       device="cpu",
   )

   # Champion configuration (OpenAI LLM selection)
   # learner = SemanticSwingersTaxonomyLearner(
   #     top_k=30, selector="openai", api_key="<OPENAI_API_KEY>",
   # )

   # Local champion-reproduction (no API key; requires a running Ollama server)
   # learner = SemanticSwingersTaxonomyLearner(
   #     top_k=30, selector="ollama",
   # )

Run the Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The learner runs on raw ontology objects, so pass ``ontologizer_data=False``.

.. code-block:: python

   from ontolearner import LearnerPipeline

   pipeline = LearnerPipeline(
       llm=learner,
       llm_id="semanticswingers-taxonomy",
       ontologizer_data=False,
   )

   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       task="taxonomy-discovery",
       evaluate=True,
       ontologizer_data=False,
   )

   print(outputs["metrics"])

Reproducibility
---------------------------------

Which selector reproduces which reported number, and what is required to run it:

- **Term typing (Task B)** — the offline ``"embedding"`` selector alone gets close to the
  competition champion on Wine (local ``≈0.687`` vs. the champion's ``0.690``). No API key
  is needed to reproduce this figure.
- **Taxonomy discovery (Task C)** — the gap is much larger: the paid champion selector
  (``"openai"``) reaches ``0.21``, while the offline ``"embedding"`` heuristic reaches only
  ``0.07``. Reproducing the champion number for this task requires an OpenAI API key (or the
  local ``"ollama"`` selector as a free, unverified approximation of the same prompting
  strategy).
- **Determinism** — both offline ``"embedding"`` selectors are fully deterministic: same
  encoder, same inputs, same outputs, every run (no sampling, ``temperature`` is irrelevant
  since no LLM is called). The ``"openai"``/``"ollama"`` selectors call ``temperature=0``
  but LLM outputs are not guaranteed bit-for-bit reproducible across provider versions.
- **API key handling** — ``selector="openai"`` reads ``api_key`` if passed explicitly,
  otherwise falls back to the ``OPENAI_API_KEY`` environment variable; if neither is set,
  the learner silently degrades to the offline ``"embedding"`` selector rather than raising,
  so pipelines never hard-fail for lack of a key. ``selector="ollama"`` never reads
  ``OPENAI_API_KEY`` and needs no key at all — only a local Ollama server.
