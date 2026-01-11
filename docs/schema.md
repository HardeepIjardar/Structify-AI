# Refined Prompt Schema — Explained

This schema is the contract between Structify AI and downstream systems.

Every field exists for a reason.
Removing any of them breaks something important.

---

## meta

Context about *how* the input was processed.

### source_types
Tracks which modalities contributed to the result.

Why it exists:
- Debugging
- Auditing
- Trust calibration

Without it, downstream systems lose traceability.

---

### confidence_score
A numeric estimate of how actionable the input is.

Why it exists:
- Enables automated rejection
- Allows routing decisions
- Prevents blind trust in weak inputs

This score is conservative by design.

---

### ambiguities_detected
Boolean shortcut for unresolved questions.

Why it exists:
- Fast checks without parsing the full payload
- Signals need for clarification

---

## intent

The semantic core of the request.

### primary_goal
The single most important field in the entire schema.

If this cannot be determined, the input is rejected.

---

### problem_statement
Why this system or feature is needed.

Helps downstream systems understand intent, not just output.

---

### target_user
Who the request is meant for.

Optional, but extremely valuable when present.

---

## functional_requirements

A list of explicit requirements derived from the input.

Each requirement has:
- a deterministic ID
- a plain description
- a priority level

At least one requirement is mandatory.
No requirements means no actionable intent.

---

## constraints

Non-functional limitations grouped by category:

- technical
- business
- design

These are structured, not inferred.

---

## inputs_provided

Summarized snapshots of the original inputs.

Why this exists:
- Traceability
- Debugging
- Human review

This prevents “black box” normalization.

---

## expected_outputs

Defines what downstream systems are expected to produce.

If deliverables are missing, the schema is invalid.

---

## open_questions

A deliberate list of unresolved ambiguities.

This system surfaces uncertainty instead of hiding it.

---

## rejection_reason

Present only when the input is rejected.

A rejected input returns **only** this field.
