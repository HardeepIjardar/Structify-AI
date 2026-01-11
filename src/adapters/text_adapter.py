import unicodedata
from src.adapters.base_adapter import BaseAdapter
from src.models import AdapterOutput


class TextAdapter(BaseAdapter):
    def normalize(self, raw_input: str) -> AdapterOutput:
        text = unicodedata.normalize("NFKC", raw_input.strip())
        text = " ".join(text.split())
        return AdapterOutput(source_type="text", content=text)
