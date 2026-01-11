from src.extractor.content_extractor import ContentExtractor
from src.refiner.semantic_refiner import SemanticRefiner
from src.assembler.schema_assembler import SchemaAssembler
from src.validator.schema_validator import SchemaValidator
from src.rejector.rejection_handler import RejectionHandler
from src.models import RejectionResponse


class NormalizationPipeline:
    async def normalize(self, request):
        extracted = ContentExtractor().extract(request)

        refined = await SemanticRefiner().refine(
            extracted.aggregated_content
        )

        schema = SchemaAssembler().assemble(refined, extracted)

        is_valid, errors, validated = SchemaValidator().validate(schema)

        rejection = RejectionHandler().check(errors)
        if rejection:
            return rejection

        return validated