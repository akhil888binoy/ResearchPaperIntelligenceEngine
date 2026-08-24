from src.database.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Column, Integer, ForeignKey 

class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String, nullable=False)
    document_id = Column(Integer, ForeignKey("documents.id", ondelete="CASCADE"), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    page_number = Column(Integer, nullable=False)
    section = Column(String, nullable=False)