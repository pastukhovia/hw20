from flask import request
from flask_restx import Resource, Namespace
from container import movie_service
from dao.model.movie import MoviesSchema

movie_ns = Namespace('movies')

movies_schema = MoviesSchema(many=True)
movie_schema = MoviesSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director')
        genre_id = request.args.get('genre')
        year = request.args.get('year')

        if director_id:
            movies = movie_service.get_all_by_director(director_id)
            return movies_schema.dump(movies), 200
        elif genre_id:
            movies = movie_service.get_all_by_genre(genre_id)
            return movies_schema.dump(movies), 200
        elif year:
            movies = movie_service.get_all_by_year(year)
            return movies_schema.dump(movies), 200
        else:
            movies = movie_service.get_all()
            return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.get_json()
        movie_service.create(req_json)

        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.get_json()
        req_json['id'] = mid

        movie_service.update(req_json)

        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)

        return '', 204
