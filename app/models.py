from dataclasses import dataclass

@dataclass
class Document:
    content: str
    metadata: dict

@dataclass
class Chunk:
    content: str
    metadata: dict
    chunk_index: int