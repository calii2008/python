from fastapi import APIRouter
from models.recipe import Recipe
from database import recipes_db

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.get("/")
def get_recipes():
    return recipes_db

@router.post("/")
def create_recipe(recipe: Recipe):
    recipes_db.append(recipe)
    return recipe