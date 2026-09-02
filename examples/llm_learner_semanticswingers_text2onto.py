"""Semantic-Swingers Task A (flagship): text2onto with the RA-FT Qwen3.5-9B generator.

Requires transformers installed from git source (no released version registers the qwen3_5
architecture yet) plus peft. See the ImportError raised by `learner.load()` for the exact
pinned pip install command, or docs/ontolearner-native-integration-poc.md in the team's main
repo (llms4ol-2026) for the full model-portability investigation:

    pip install "transformers @ git+https://github.com/huggingface/transformers.git@\
<pinned commit — see SemanticSwingersText2OntoLearner._VERIFIED_TRANSFORMERS_COMMIT>" \
"peft>=0.19" "accelerate>=1.0"

The `adapter` argument accepts a local filesystem path (fastest way to try this without HF
access — point it at the team's `data/ft/_runners/raft_adapter/final` or `baseft_adapter/final`)
or a HuggingFace repo id once the adapters are published (see yp4).
"""

from ontolearner import LearnerPipeline
from ontolearner.learner.text2onto import SemanticSwingersText2OntoLearner

# ---- Toy document set (self-contained; swap in the competition's real train/test docs) ----
train_data = {
    "documents": [
        {
            "doc_id": "d1",
            "text": "A poodle is a dog. A dog is a mammal. A mammal is an animal.",
        },
    ],
    "triples": {
        "d1": [
            ["poodle", "is-a", "dog"],
            ["dog", "is-a", "mammal"],
            ["mammal", "is-a", "animal"],
        ],
    },
}
test_data = {
    "documents": [
        {
            "doc_id": "d2",
            "text": "A tabby is a cat. A cat is a mammal.",
        },
    ],
}

# ---- Configure the learner ----
# RA-FT (competition champion): trained WITH exemplars baked into the prompt, wants top_k > 0.
# Swap adapter="baseft", top_k=0 for the retrieval-free standard fine-tune instead.
learner = SemanticSwingersText2OntoLearner(
    adapter="raft",  # or a local path, e.g. "../llms4ol-2026/data/ft/_runners/raft_adapter/final"
    top_k=1,
    device="cpu",  # "cuda" strongly recommended — see the class docstring on CPU speed
)

pipeline = LearnerPipeline(
    llm=learner,
    llm_id="semanticswingers-text2onto",
    ontologizer_data=False,
)

outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    task="text2onto",
    evaluate=False,  # no gold terms2docs/terms2types provided for this toy example
    ontologizer_data=False,
)

print(outputs["predictions"])
print("Elapsed time:", outputs["elapsed_time"])

# ---- The same learner also serves taxonomy-discovery (composed, not a rewrite) ----
# from ontolearner import Wine, train_test_split
#
# wine = Wine()
# wine.load()
# wine_train, wine_test = train_test_split(wine.extract(), test_size=0.2, random_state=42)
#
# taxonomy_outputs = pipeline(
#     train_data=wine_train,
#     test_data=wine_test,
#     task="taxonomy-discovery",
#     evaluate=True,
#     ontologizer_data=False,
# )
# print(taxonomy_outputs["metrics"])
