from flask_restx import Namespace, Resource
from container import genre_service
from dao.model.genre import GenresSchema


genre_ns = Namespace('genres')

genre_schema = GenresSchema()
genres_schema = GenresSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres)


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre)
