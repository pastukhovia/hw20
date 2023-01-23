from unittest.mock import MagicMock
import pytest

from dao.model.genre import Genre

from dao.genre import GenreDAO
from services.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    director_1 = Genre(id=1, name='Test')
    director_2 = Genre(id=2, name='Test')

    genre_dao.get_one = MagicMock(return_value=director_1)
    genre_dao.get_all = MagicMock(return_value=[director_1, director_2])

    return genre_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 1
