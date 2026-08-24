from src.database.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Column, Integer, DateTime , ForeignKey , Float

class RetrievalResult(Base):
    __tablename__ = "retrieval_results"

    id = Column(Integer, primary_key=True, nullable=False)
    chunk_id = Column(Integer, ForeignKey("chunks.id", ondelete="CASCADE"), nullable=False)
    score = Column(Float, nullable=False)
    rank = Column(Integer, nullable=False)
    retrieval_method  = Column(String, nullable=False)