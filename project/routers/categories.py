from fastapi import APIRouter
from models.category import Category
from database import categories_db

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/")
def get_categories():
    return categories_db

@router.post("/")
def create_category(category: Category):
    categories_db.append(category)
    return category