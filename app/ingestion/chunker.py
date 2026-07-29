from abc import ABC, abstractmethod
from app.models import Document, Chunk
from langchain_core.documents import Document as LCDocument
from langchain_text_splitters import RecursiveCharacterTextSplitter

class BaseChunker(ABC):
    @abstractmethod
    def split(self, document: Document) -> list[Chunk]:
        pass

class RecursiveTokenChunker(BaseChunker):
    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=100):
        self.splitter = RecursiveCharacterTextSplitter.fromtiktoken_encoder(
            encoding_name="cl100k_base",
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, document: Document) -> list[Chunk]:
        lc_document = LCDocument(page_content=document.content, metadata=document.metadata)
        lc_chunks = self.splitter.split_documents([lc_document])
        result = []
        for index, chunk in enumerate(lc_chunks):
            result.append(Chunk(content=chunk.page_content, metadata=chunk.metadata, chunk_index=index))
        return result
