# Assumptions & Design Decisions

This document captures intentional trade-offs.

Nothing here is accidental.

---

## Operating Assumptions

- The system is used internally
- Inputs are frequently low quality
- Downstream systems require strict guarantees
- Human clarification may happen later

---

## Key Trade-offs

### Determinism over expressiveness
The system prefers predictable output over rich interpretation.

---

### Rejection over forced normalization
Invalid input is rejected instead of being coerced into structure.

---

### Minimal extraction over hallucination
When information is unclear, the system does not guess.

It asks questions.

---

## LLM-Related Assumptions

- LLM output is untrusted
- LLM assists, it does not decide
- All enforcement is deterministic
- The system remains functional even with weak LLM output

---

## Scalability Assumptions

- Stateless execution
- In-memory processing
- Single refinement per request

These choices simplify reasoning and testing.

---

## Explicitly Out of Scope

- Persistent storage
- Authentication and authorization
- Model fine-tuning
- Multi-turn clarification loops
- Real-time collaboration
