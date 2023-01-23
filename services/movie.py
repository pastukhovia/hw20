class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all_by_director(self, director_id):
        return self.dao.get_all_by_director(director_id)

    def get_all_by_genre(self, genre_id):
        return self.dao.get_all_by_genre(genre_id)

    def get_all_by_year(self, year):
        return self.dao.get_all_by_year(year)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        mid = int(data['id'])
        movie = self.get_one(mid)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
