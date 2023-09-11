from pydantic import BaseModel

class PersonBase(BaseModel):
    """
    Common properties for PersonCreate and Person models.
    """
    name: str


class PersonCreate(PersonBase):
    """
    Schema for creating a new Person.
    """


class Person(PersonBase):
    """
    Person schema with an 'id' field. (ORM mode enabled)
    """
    id: int

    class Config:
        orm_mode = True
