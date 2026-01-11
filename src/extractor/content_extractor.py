from src.adapters.text_adapter import TextAdapter
from src.adapters.image_adapter import ImageAdapter
from src.adapters.document_adapter import DocumentAdapter
from src.models import ExtractedContent, NormalizeRequest


class ContentExtractor:
    def extract(self, request: NormalizeRequest) -> ExtractedContent:
        contents = []
        source_types = []

        text_summary = image_summary = document_summary = ""

        if request.text:
            res = TextAdapter().normalize(request.text)
            contents.append(res.content)
            source_types.append("text")
            text_summary = res.content[:200]

        if request.image:
            res = ImageAdapter().normalize(request.image)
            contents.append(res.content)
            source_types.append("image")
            image_summary = res.content

        if request.document:
            res = DocumentAdapter().normalize(request.document)
            contents.append(res.content)
            source_types.append("document")
            document_summary = res.content[:200]

        if not contents:
            raise ValueError("No valid input provided")

        return ExtractedContent(
            aggregated_content="\n\n---\n\n".join(contents),
            source_types=source_types,
            text_summary=text_summary,
            image_summary=image_summary,
            document_summary=document_summary,
        )
