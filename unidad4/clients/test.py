import requests
from getpass import getpass


endpoint_add_movie = 'http://127.0.0.1:8000/api/movies/create/'
endpoint_retrieve_movie = 'http://127.0.0.1:8000/api/movies/2/'
endpoint_update_movie = 'http://127.0.0.1:8000/api/movies/1/update/'
endpoint_delete_movie = 'http://127.0.0.1:8000/api/movies/1/delete/'
endpoint_add_genre = 'http://127.0.0.1:8000/api/genres/create/'
endpoint_retrieve_genre = 'http://127.0.0.1:8000/api/genres/1/'
endpoint_update_genre = 'http://127.0.0.1:8000/api/movies/1/genres/'
endpoint_delete_genre = 'http://127.0.0.1:8000/api/genres/delete/'

endpoint_api_view = 'http://127.0.0.1:8000/api/genres/1/movies/'

endpoint_movies_viewset = 'http://127.0.0.1:8000/api/movies_viewset'

endpoint_auth_token = 'http://127.0.0.1:8000/api/auth/'

username = input('Usuario:')
password = getpass('Contraseña: ')

token_res = requests.post(endpoint_auth_token, json = {'username':username, 'password':password})
print(token_res.json())

if token_res.status_code == 200:
    token = token_res.json()['token']
    headers = {
        "Authorization": f'token {token}'
    }
    response = requests.get(endpoint_movies_viewset, headers = headers)
    print(response.json()) 