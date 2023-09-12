from sqlalchemy import Column, String, Integer

from .database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, unique=True, index=True)
