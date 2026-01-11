from src.models import (
    RefinedPromptSchema, Meta, Intent, Constraints,
    InputsProvided, ExpectedOutputs, FunctionalRequirement
)


class SchemaAssembler:
    def assemble(self, refined, extracted):
        requirements = [
            FunctionalRequirement(
                id=f"FR-{i+1:03d}",
                description=r["description"],
                priority=r.get("priority", "should")
            )
            for i, r in enumerate(refined.requirements)
        ]

        return RefinedPromptSchema(
            meta=Meta(
                source_types=extracted.source_types,
                confidence_score=refined.confidence_score,
                ambiguities_detected=bool(refined.open_questions),
            ),
            intent=Intent(
                primary_goal=refined.primary_goal,
                problem_statement=refined.problem_statement,
                target_user=refined.target_user,
            ),
            functional_requirements=requirements,
            constraints=Constraints(
                technical=refined.technical_constraints,
                business=refined.business_constraints,
                design=refined.design_constraints,
            ),
            inputs_provided=InputsProvided(
                text_summary=extracted.text_summary,
                image_summary=extracted.image_summary,
                document_summary=extracted.document_summary,
            ),
            expected_outputs=ExpectedOutputs(
                deliverables=refined.deliverables,
                format=refined.output_format,
            ),
            open_questions=refined.open_questions,
        )
