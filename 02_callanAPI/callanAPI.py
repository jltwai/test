import requests

api_key = "f57434a8e5e140eff850183e10797005"

# HTTP requests methods
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
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)
r = requests.get(endpoint) # json={"api_key": api_key}
print(r.status_code)
print(r.text)