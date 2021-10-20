# HTTP requests
from tmdb import getMovie
"""
GET -> grab data
POST -> add/update data

PATCH
PUT
DELETE
"""
# what's the endpoint (or a url)?

# what is the HTTP method that I need?


"""
Endpoint
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=f57434a8e5e140eff850183e10797005
"""
movie_id = 500
r = getMovie(movie_id)
print(r.status_code)
print(r.text)

r = getMovie(499)
print(r.status_code)
print(r.text)