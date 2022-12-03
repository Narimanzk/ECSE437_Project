from pydantic import BaseModel


class Movie(BaseModel):
    title: str = None
    director: str = None
    year: int = None
    genre: str = None