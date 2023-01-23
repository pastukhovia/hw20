from unittest.mock import MagicMock
import pytest

from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre

from dao.movie import MovieDAO
from services.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Test', year=2000, director_id=1, genre_id=2)
    movie_2 = Movie(id=2, title='Test', year=2001, director_id=1, genre_id=1)
    movie_3 = Movie(id=3, title='Test', year=2000, director_id=2, genre_id=2)

    genre_1 = Genre(id=1, name='Test')
    genre_2 = Genre(id=2, name='Test')

    director_1 = Director(id=1, name='Test')
    director_2 = Director(id=2, name='Test')

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.get_all_by_year = MagicMock(return_value=[movie_1, movie_3])
    movie_dao.get_all_by_director = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.get_all_by_genre = MagicMock(return_value=[movie_1, movie_3])
    movie_dao.create = MagicMock()
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 1

    def test_get_all_by_year(self):
        movies = self.movie_service.get_all_by_year(2000)

        assert len(movies) > 1

    def test_get_all_by_director(self):
        movies = self.movie_service.get_all_by_director(2)

        assert len(movies) > 1

    def test_get_all_by_genre(self):
        movies = self.movie_service.get_all_by_genre(2)

        assert len(movies) > 1

    def test_create(self):
        movie = {
            'title': 'test'
        }

        self.movie_service.create(movie)

    def test_update(self):
        movie = {
            "title": "Йеллоустоун",
            "description": "Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
            "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
            "year": 2018,
            "rating": 8.6,
            "genre_id": 17,
            "director_id": 1,
            "id": 1
        }

        self.movie_service.update(movie)

    def test_delete(self):
        self.movie_service.delete(1)
