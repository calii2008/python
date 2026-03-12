from pydantic import BaseModel

class Recipe(BaseModel):
    id: int
    title: str
    description: str
    category_id: int