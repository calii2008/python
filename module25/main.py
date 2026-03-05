import database
import models
from models import movie, movieCriate

.app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the movies Crud API"}


@app.post("/movies/", response_model=movie)
def create_movie)(movie: MovieCreate, movie_id=none):
   """ceates a new movie in the database"""
    movie_id - database.create_movie(movie)
    return models.movie(id.movie_id, **movie.dite())



@app.get("/movies/", )






























