from io import BytesIO
import base64
from PyPDF2 import PdfReader
from docx import Document
from src.adapters.base_adapter import BaseAdapter
from src.models import AdapterOutput


class DocumentAdapter(BaseAdapter):
    def normalize(self, raw_input: str) -> AdapterOutput:
        data = base64.b64decode(raw_input)
        text = ""

        try:
            reader = PdfReader(BytesIO(data))
            for page in reader.pages:
                text += page.extract_text() or ""
        except Exception:
            doc = Document(BytesIO(data))
            for p in doc.paragraphs:
                text += p.text + "\n"

        return AdapterOutput(source_type="document", content=text.strip())
