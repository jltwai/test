import requests

api_key = "f57434a8e5e140eff850183e10797005"

def getMovie(movie_id):
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    print(endpoint)
    return requests.get(endpoint) # json = {"api_key": api_key}