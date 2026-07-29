from abc import ABC, abstractmethod
from pathlib import Path


class BaseParser(ABC):
    @abstractmethod
    def parse(self, file_path: Path) -> str:
        pass


class MarkdownParser(BaseParser):
    def parse(self, file_path: Path) -> str:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()


class PDFParser(BaseParser):
    def parse(self, file_path: Path) -> str:
        raise NotImplementedError("PDF parser not implemented yet")


class DocxParser(BaseParser):
    def parse(self, file_path: Path) -> str:
        raise NotImplementedError("DOCX parser not implemented yet")