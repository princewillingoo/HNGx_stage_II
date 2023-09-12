from sqlalchemy.orm import Session
from sqlalchemy import or_

from . import models


def get_person(db: Session, id: int):
    return db.query(models.Person).filter(models.Person.id == id)


def get_person_by_name(db: Session, name: str):
    return db.query(models.Person).filter(models.Person.name == name)


# def get_person_by_name_or_id(db: Session, id: str):
#     db_person = db.query(models.Person).filter(or_(models.Person.id == id, models.Person.name == id))

#     return db_person
