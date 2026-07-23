"""Extending the Semantic-Swingers Task A learner for *your own* experiments.

The learner is deliberately configuration-driven: base model, adapter, generation backend,
retriever, training regime, the extraction **prompt**, and the relation set that projects to
`types` are all constructor arguments. So most adaptations need **no subclassing at all** — you
pass different arguments. This file shows the three levels of customization, cheapest first.

Run with a local Ollama (`ollama serve` + a small model) so it needs no API key or GPU.
"""

from ontolearner.learner.text2onto import SemanticSwingersText2OntoLearner


# ---------------------------------------------------------------------------------------------
# Level 1 — same method, YOUR model / backend / retriever (no code, just arguments)
# ---------------------------------------------------------------------------------------------
# Swap the generator (any OpenAI-compatible endpoint via backend="ollama"/"openai", any local
# checkpoint via backend="peft"/"mlx"), the retriever encoder, and how many exemplars to use.
learner = SemanticSwingersText2OntoLearner(
    backend="ollama",
    llm_model="llama3.1:8b",                                   # <- your generator
    retriever_model_id="sentence-transformers/all-mpnet-base-v2",  # <- your retriever
    top_k=5,
)


# ---------------------------------------------------------------------------------------------
# Level 2 — YOUR domain: a different extraction prompt and a different relation vocabulary
# ---------------------------------------------------------------------------------------------
# `system_prompt` replaces the extraction instructions; `typing_relations` controls which
# relations count as term→type edges when projecting to OntoLearner's {terms, types} shape.
# Neither requires touching the package.
MY_PROMPT = (
    "You are a biomedical ontology engineer. Extract triples [subject, relation, object] using "
    "ONLY these relations: rdfs:subClassOf, rdf:type, part_of. "
    'Output ONLY JSON {"triples": [[s, r, o], ...]}.'
)
domain_learner = SemanticSwingersText2OntoLearner(
    backend="ollama",
    llm_model="llama3.1:8b",
    system_prompt=MY_PROMPT,                                   # <- your instructions
    typing_relations={"rdf:type", "rdfs:subClassOf"},          # <- your typing relations
)


# ---------------------------------------------------------------------------------------------
# Level 3 — YOUR pipeline: subclass to change one step, reuse the rest
# ---------------------------------------------------------------------------------------------
# When a *behaviour* needs to change (not just a value), override a single method. Everything
# else — retrieval, backend dispatch, training, the {terms, types} projection — is inherited.
class MyText2OntoLearner(SemanticSwingersText2OntoLearner):
    """Example: post-filter generated triples to a relation allow-list of your choosing."""

    ALLOW = {"rdf:type", "rdfs:subClassOf", "part_of"}

    def _generate_triples(self, text, exemplars):
        triples = super()._generate_triples(text, exemplars)   # reuse the whole generation path
        return [(s, r, o) for (s, r, o) in triples if r in self.ALLOW]


# ---------------------------------------------------------------------------------------------
# Training your own adapter is one more argument, not a separate script (train_mode + fit()).
# ---------------------------------------------------------------------------------------------
#   trainer = SemanticSwingersText2OntoLearner(
#       train_mode="raft",           # or "baseft"
#       train_backend="mlx",         # or "peft" (CUDA)
#       output_dir="my_adapter",
#       system_prompt=MY_PROMPT,     # trains against YOUR prompt
#   )
#   trainer.fit(train_docs, task="text2onto")   # builds pairs (leave-one-out for raft) -> trains -> loads

if __name__ == "__main__":
    print("Level 1 learner:", learner.llm_model, "top_k", learner.top_k)
    print("Level 2 typing relations:", sorted(domain_learner.typing_relations))
    print("Level 3 subclass:", MyText2OntoLearner().__class__.__name__)
