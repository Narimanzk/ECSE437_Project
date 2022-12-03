import uvicorn

from src.client.external_movie_client import ExternalMovieClient
from src.client.postgres_client import PostgresClient
from src.config.external_movies_client_config import ExternalMovieClientConfig
from src.config.postgres_client_config import PostgresClientConfig
from src.repository.movie_repository import MovieRepository
from src.rest_api.movie_rest_api import MovieRestApi
from src.service.movie_service import MovieService


def start_application() -> MovieRestApi:
    postgres_url = "localhost"
    postgres_port = "5433"
    postgres_database = "movieApp"
    postgres_user_name = "username"
    postgres_password = "password"

    external_client_url = "http://localhost"
    external_client_port = 8000

    postgres_client_config = PostgresClientConfig(url=postgres_url,
                                                  port=postgres_port,
                                                  database=postgres_database,
                                                  user_name=postgres_user_name,
                                                  password=postgres_password)
    postgres_client = PostgresClient(postgres_client_config)
    movie_repository = MovieRepository(postgres_client=postgres_client)

    external_movie_client_config = ExternalMovieClientConfig(url=external_client_url, port=external_client_port)
    external_movie_client = ExternalMovieClient(external_movie_client_config)

    movie_service = MovieService(movie_repository=movie_repository,
                                       external_movie_client=external_movie_client)
    movie_rest_api = MovieRestApi(movie_service=movie_service)
    return movie_rest_api


if __name__ == "__main__":
    uvicorn.run(app=start_application())