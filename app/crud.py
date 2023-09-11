from sqlalchemy.orm import Session

from . import models, schemas


def get_person(db: Session, person_id: int):
    return db.query(models.person).filter(models.person.id == person_id).first()


def get_person_by_name(db: Session, name: str):
    return db.query(models.person).filter(models.person.name == name).first()


def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.personCreate):
    db_person = models.person(name=person.name)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person