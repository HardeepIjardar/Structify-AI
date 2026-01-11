# AI Usage & Containment Strategy

Structify AI uses AI carefully and reluctantly.

This is intentional.

---

## Where AI Is Used

AI is used **only** in the semantic refinement stage to:

- interpret natural language
- extract intent and requirements
- identify ambiguity
- estimate confidence

AI never produces final outputs.

---

## Where AI Is NOT Used

AI is explicitly excluded from:

- schema construction
- validation
- rejection decisions
- output formatting

All of these are deterministic.

---

## Why AI Is Constrained

Unconstrained AI:
- hallucinates
- hides uncertainty
- breaks invariants

This system assumes AI can be wrong.

Everything critical is verified independently.

---

## Hallucination Control Mechanisms

- AI outputs plain text, not JSON
- Parsing is strict and validated
- Schema assembly is handwritten
- Business rules override AI output
- Low-confidence inputs are rejected early

---

## Conservative Extraction by Design

When semantic confidence is moderate, the system intentionally:

- avoids enriching requirements
- avoids differentiating features
- flags ambiguity instead

This behavior is deliberate and documented.

Silence is safer than invention.
