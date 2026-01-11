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

## Sample Input/Output

### Example 1: Well-Specified Input (High Confidence)

**Input:**
```bash
python -m src.main "Build a web-based task management system for small teams using a REST-based backend and a browser-based frontend. Users authenticate via login, create projects, assign tasks, track status (todo, in progress, completed), set deadlines, and receive deadline notifications. The system supports role-based access with admins managing users and projects. No mobile support is required. Initial version targets teams under 50 users."
```

**Output:**
```json
{
  "meta": {
    "source_types": ["text"],
    "confidence_score": 0.9,
    "ambiguities_detected": false
  },
  "intent": {
    "primary_goal": "Build a software system",
    "problem_statement": "User described a system to be built",
    "target_user": "End users"
  },
  "functional_requirements": [
    {
      "id": "FR-001",
      "description": "User login",
      "priority": "must"
    },
    {
      "id": "FR-002",
      "description": "Status tracking",
      "priority": "must"
    },
    {
      "id": "FR-003",
      "description": "Deadline management",
      "priority": "must"
    },
    {
      "id": "FR-004",
      "description": "Notifications",
      "priority": "must"
    },
    {
      "id": "FR-005",
      "description": "Role-based access",
      "priority": "must"
    },
    {
      "id": "FR-006",
      "description": "Admin controls",
      "priority": "must"
    }
  ],
  "constraints": {
    "technical": [],
    "business": [],
    "design": []
  },
  "inputs_provided": {
    "text_summary": "Build a web-based task management system for small teams using a REST-based backend and a browser-based frontend. Users authenticate via login, create projects, assign tasks, track status (todo, in progress, completed), set deadlines, and receive deadline notifications. The system supports role-based access with admins managing users and projects. No mobile support is required. Initial version targets teams under 50 users.",
    "image_summary": "",
    "document_summary": ""
  },
  "expected_outputs": {
    "deliverables": ["Working application"],
    "format": "Web application"
  },
  "open_questions": [],
  "rejection_reason": null
}
```

**Result:** High confidence (0.9), no ambiguities detected. System extracted 6 specific functional requirements from the detailed description without hallucinating.

---

### Example 2: Moderate Confidence with Ambiguities

**Input:**
```bash
python -m src.main "Build a task management system for teams where users can create tasks, assign them to others, track progress, and manage deadlines. The system should be easy to use and suitable for general productivity needs."
```

**Output:**
```json
{
  "meta": {
    "source_types": ["text"],
    "confidence_score": 0.3,
    "ambiguities_detected": true
  },
  "intent": {
    "primary_goal": "Build a software system",
    "problem_statement": "User described a system to be built",
    "target_user": "End users"
  },
  "functional_requirements": [
    {
      "id": "FR-001",
      "description": "Deadline management",
      "priority": "must"
    }
  ],
  "constraints": {
    "technical": [],
    "business": [],
    "design": []
  },
  "inputs_provided": {
    "text_summary": "Build a task management system for teams where users can create tasks, assign them to others, track progress, and manage deadlines. The system should be easy to use and suitable for general productivity needs.",
    "image_summary": "",
    "document_summary": ""
  },
  "expected_outputs": {
    "deliverables": ["Working application"],
    "format": "Web application"
  },
  "open_questions": ["Architecture unspecified"],
  "rejection_reason": null
}
```

**Result:** Lower confidence (0.3) due to vague terms like "easy to use" and missing architecture details. System flags ambiguity but still generates schema. Only 1 requirement extracted from keyword matching.

---

### Example 3: Irrelevant/Motivational Input (Rejected)

**Input:**
```bash
python -m src.main "You are doing amazing, keep going!"
```

**Output:**
```json
{
  "rejection_reason": "Input rejected: confidence_score below actionable threshold"
}
```

**Result:** Input correctly identified as non-actionable and rejected. No schema returned.  
Downstream systems are protected from meaningless input.

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
