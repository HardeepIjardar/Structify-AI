from src.extractor.content_extractor import ContentExtractor
from src.refiner.semantic_refiner import SemanticRefiner
from src.assembler.schema_assembler import SchemaAssembler
from src.validator.schema_validator import SchemaValidator
from src.rejector.rejection_handler import RejectionHandler
from src.models import RejectionResponse


class NormalizationPipeline:
    async def normalize(self, request):
        # Stage 2: Extract
        extracted = ContentExtractor().extract(request)

        # Stage 3: Semantic refinement
        refined = await SemanticRefiner().refine(extracted.aggregated_content)

        # 🔴 EARLY REJECTION GATE (CRITICAL)
        if refined.confidence_score < 0.2:
            return RejectionResponse(
                rejection_reason="Input rejected: confidence_score below actionable threshold"
            )

        # Stage 4: Assemble
        schema = SchemaAssembler().assemble(refined, extracted)

        # Stage 5: Validate
        is_valid, errors, validated = SchemaValidator().validate(schema)

        # Stage 6: Final rejection check
        rejection = RejectionHandler().check(errors)
        if rejection:
            return rejection

        return validated
