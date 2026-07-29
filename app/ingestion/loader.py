from pathlib import Path
from app.models import Document
from app.ingestion.parser import (
    MarkdownParser,
    PDFParser,
    DocxParser,
)

class DocumentLoader:
    def __init__(self, data_directory:str):
        self.data_directory = Path(data_directory)
        self.parsers = {
            ".md": MarkdownParser(),
            ".pdf": PDFParser(),
            ".docx": DocxParser(),
        }

    def load(self):
        documents = []
        files=self._discover_files()
        for file in files:
            content = self._parse_file(file)
            if not content.strip():
                continue

            document = self._create_document(file,content)
            documents.append(document)
        return documents

    def _discover_files(self):
        return list(self.data_directory.rglob('*.md')) + list(self.data_directory.rglob('*.pdf'))

    def _parse_file(self, file_path: Path) -> str:
        parser = self.parsers.get(file_path.suffix.lower())
        if parser is None:
            raise ValueError(
                f"No parser available for {file_path.suffix}")
        return parser.parse(file_path)

    def _create_document(self, filepath:Path, content:str):
        metadata = {
            "filename": filepath.name,
            "category": filepath.parent.name,
            "source": str(filepath),
            "extension": filepath.suffix
        }
        return Document(content=content, metadata=metadata)