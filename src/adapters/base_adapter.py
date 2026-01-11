from abc import ABC, abstractmethod
from src.models import AdapterOutput


class BaseAdapter(ABC):
    @abstractmethod
    def normalize(self, raw_input: str) -> AdapterOutput:
        pass
