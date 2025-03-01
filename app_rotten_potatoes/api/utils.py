from ..models import Movie, Review

def search_movie(title, requests):
    api_key = 'c31f0ffb'
    api_url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(api_url)
    return response.json()

def save_movie(data):
    title_create = data.get('Title')
    genre_create = data.get('Genre')
    year_create = data.get('Year')
    director_create = data.get('Director')
    imdb_rating_create = data.get('imdbRating')

    movie_database = Movie(title=title_create, genre=genre_create, year=year_create, director=director_create, imdb_rating=imdb_rating_create)
    movie_database.save()