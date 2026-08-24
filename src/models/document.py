from src.database.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Column, Integer, DateTime

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    source  = Column(String, nullable=False)