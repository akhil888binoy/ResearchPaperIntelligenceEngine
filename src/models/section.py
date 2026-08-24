from src.database.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Column, Integer, DateTime

class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, nullable=False)
    introduction = Column(String, nullable=False)
    methodology = Column(String, nullable=False)
    results = Column(String, nullable=False)
    conclusion = Column(String, nullable=False)