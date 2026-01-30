from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

from contextlib import asynccontextmanager

from sqlalchemy import text

# 1: database config

import os  
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not found in .env file")

engine = create_engine(DATABASE_URL)

# 2: define a table
class Item (SQLModel, table = True):
    id: int = Field (default = None, primary_key = True)
    name: str = Field (index = True)
    description: str | None = None

# 3: create db and tables 
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
# 4: get a db session
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager 
async def lifespan (app : FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("connection succesful!")
    except Exception as e:
        print(f"connection failed! {e}")
    # start-up
    create_db_and_tables()
    
    yield
    #shut-down
    engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.post("/items/")
def create_item(item : Item, session : SessionDep):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.get("/items")
def read_items(session : SessionDep) -> list[Item]:
    return session.exec(select(Item)).all()

@app.get("/items/{item_id}", response_model = Item)
def read_item(item_id : int, session : SessionDep):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.patch("/items/{item_id}", response_model = Item)
def update_item(item_id : int, item_data : Item, session: SessionDep):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    new_data = item_data.model_dump(exclude_unset=True)
    
    for key, value in new_data.items():
        setattr(db_item, key, value)
    
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, session: SessionDep):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    session.delete(item)
    session.commit()
    return {"ok": True}


