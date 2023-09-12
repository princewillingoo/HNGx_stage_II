from fastapi import Depends, FastAPI, HTTPException, Response, APIRouter
from sqlalchemy.orm import Session

from . import models, schemas, utils
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create
@app.post("/api/", response_model=schemas.Person, status_code=201)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = utils.get_person_by_name(db, name=person.name).first()

    if db_person:
        raise HTTPException(status_code=400, detail="Name Already Registered")

    db_person = models.Person(name=person.name)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)

    return db_person


# read
@app.get("/api/{id}/", response_model=schemas.Person, status_code=200)
def read_person(id: int, db: Session = Depends(get_db)):
    db_person = utils.get_person(db, id=id).first()
    
    if db_person == None:
        raise HTTPException(status_code=404, detail="Person Does Not Exist")
    
    return db_person


# update
@app.put("/api/{id}/", response_model=schemas.Person, status_code=200)
def update_person(
    id: int, updated_person: schemas.PersonUpdate, db: Session = Depends(get_db)
):
    db_person = utils.get_person(db, id=id)
    person = db_person.first()

    if person == None:
        raise HTTPException(
            status_code=404, detail=f"Person With ID:{id} Was Not Found"
        )

    # Check if the updated name is already in use
    existing_person = (
        db.query(models.Person)
        .filter(models.Person.name == updated_person.name, models.Person.id != id)
        .first()
    )

    if existing_person:
        raise HTTPException(status_code=400, detail="Name Already Registered")

    db_person.update(updated_person.model_dump(), synchronize_session=False)
    db.commit()

    return db_person.first()


# delete
@app.delete("/api/{id}/", status_code=204)
def delete_post(id: int, db: Session = Depends(get_db)):
    db_person = utils.get_person(db, id=id)

    if db_person.first() == None:
        raise HTTPException(
            status_code=404, detail=f"Person With ID:{id} Was Not Found"
        )

    db_person.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=204)
