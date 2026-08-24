from src.database.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Column, Integer, DateTime

class RetrievalResult(Base):
    __tablename__ = "retrieval_results"

    id = Column(Integer, primary_key=True, nullable=False)
    chunk = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=False)
    retrieval_method  = Column(String, nullable=False)