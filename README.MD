# Structify AI

**Structify AI** is an internal Prompt Normalization Engine designed to sit at the boundary between raw user input and downstream AI systems.

It converts unstructured, multi-modal inputs into a strict, validated, machine-consumable prompt schema — or explicitly rejects the input when it is irrelevant, ambiguous, or non-actionable.

This system is intentionally conservative.  
Rejection is a feature, not a failure.

---

## Why This Exists

Most AI failures do not happen at inference time.  
They happen **before** the model is even called.

User inputs are often:
- vague
- incomplete
- overly conversational
- or completely irrelevant

Passing such inputs directly to AI systems causes hallucinations, brittle behavior, and silent failures.

Structify AI acts as a **gatekeeper**.

If an input cannot be trusted, it is stopped early with a clear technical reason.

---

## What This System Does

- Normalizes unstructured text into a strict schema
- Extracts intent, requirements, and constraints
- Tracks ambiguity explicitly instead of hiding it
- Assigns a confidence score to every input
- Rejects low-confidence or irrelevant prompts deterministically

---

## What This System Does NOT Do

- It does NOT generate final solutions
- It does NOT invent missing requirements
- It does NOT act as an autonomous AI agent
- It does NOT claim production readiness
- It does NOT depend on local models or user setup

This is an **internal engineering system**, not a consumer product.

---

## High-Level Architecture

Below is the full control flow of the system.  
This diagram shows **where AI is used** and **where determinism begins**.

```
        ┌────────────┐
        │ User Input │
        └─────┬──────┘
              │
              ▼
        ┌──────────────┐
        │    Input     │
        │   Adapters   │
        │  (Text/Image/│
        │  Document)   │
        └─────┬────────┘
              │
              ▼
        ┌────────────────┐
        │    Content     │
        │   Extraction   │
        └─────┬──────────┘
              │
              ▼
        ┌────────────────────────┐
        │ Semantic Refinement    │
        │  (LLM-Assisted,        │
        │  Plain Text Output)    │
        └─────┬──────────────────┘
              │
              ▼
        ┌────────────────┐
        │     Schema     │
        │    Assembly    │
        │ (Deterministic)│
        └─────┬──────────┘
              │
              ▼
        ┌────────────────┐
        │   Validation   │
        │  (Hard Rules)  │
        └─────┬──────────┘
              │
              ▼
        ┌───────────────┐
        │   Decision    │
        │     Node      │
        ├─────────┬─────┤
        │ Reject  │ OK  │
        │         │     │
        ▼         ▼     ▼
      Reason     End  Refined
                      Schema
```

Key property:  
**LLMs never produce final JSON.**  
All enforcement is deterministic.

---

## Design Principles

- **Determinism over cleverness**  
- **Rejection over forced normalization**  
- **Explicit ambiguity over silent guessing**  
- **Validation over trust**

This system assumes AI can be wrong.

---

## Example Behavior

### Valid but Ambiguous Input

```
Build a task management tool for small teams
```

Result:
- Schema generated
- Confidence score reduced
- Ambiguities explicitly listed
- No hallucinated features

---

### Irrelevant Input

```
You are doing amazing, keep going!
```

Result:
```json
{
  "rejection_reason": "Input rejected: confidence_score below actionable threshold"
}
```

No schema is returned.  
Downstream systems are protected.

---

## Tech Stack

- Python 3.10+
- FastAPI (API-first)
- Pydantic (schema enforcement)
- Single LLM abstraction (semantic refinement only)
- In-memory execution (no persistence)

---

## Repository Structure

```
src/
├── adapters/        # Input normalization
├── extractor/       # Content aggregation
├── refiner/         # LLM-assisted interpretation
├── assembler/       # Deterministic schema construction
├── validator/       # Hard validation rules
├── rejector/        # Explicit rejection handling
├── pipeline.py      # End-to-end orchestration
├── api.py           # REST interface
└── main.py          # CLI entrypoint
```

---

## How to Run (CLI)

```bash
python -m src.main "Build a dashboard for tracking inventory"
```

---

## How to Run (API)

```bash
uvicorn src.api:app --reload
```

POST `/normalize` with a JSON body.

---

## Documentation

Detailed design rationale and decisions are documented in:

- `docs/design.md`
- `docs/schema.md`
- `docs/assumptions.md`
- `docs/ai-usage.md`
