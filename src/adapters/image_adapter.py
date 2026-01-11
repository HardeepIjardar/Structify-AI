from src.adapters.base_adapter import BaseAdapter
from src.models import AdapterOutput


class ImageAdapter(BaseAdapter):
    def normalize(self, raw_input: str) -> AdapterOutput:
        return AdapterOutput(
            source_type="image",
            content="[Image analysis placeholder - integrate vision API]"
        )
