import idlelib.run

from pydantic import BaseModel

class MoviewCreate(BaseModel):
    title: str
    director: str

class Movie(MovieCreate):
    id:int
