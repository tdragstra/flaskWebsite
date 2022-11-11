import tmdbsimple as tmdb

tmdb.API_KEY = '7c5af9912d5af10f2663e9d2092f207b'

def movie(id):
  movie = tmdb.Movies(id).info()

  return f"""
  <div>
    <h1>{movie['title']}</h1>
    <img src='https://image.tmdb.org/t/p/w500/{movie['poster_path']}' width=200 />
    <p>⭐ {round((movie['vote_average'] / 2), 1)} / 5 of {movie['vote_count']} votes </p>
    <p>{movie['overview']}</p>
  </div>
  """

