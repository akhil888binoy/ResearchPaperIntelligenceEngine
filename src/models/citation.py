from src.database.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Column, Integer, DateTime , ForeignKey

class Citation(Base):
    __tablename__ = "citations"

    id = Column(Integer, primary_key=True, nullable=False)
    chunk_id = Column(Integer, ForeignKey("chunks.id", ondelete="CASCADE"), nullable=False)
