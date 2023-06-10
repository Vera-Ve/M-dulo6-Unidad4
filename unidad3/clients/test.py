import requests



endpoint_add_movie = 'http://127.0.0.1:8000/api/movies/create/'
endpoint_retrieve_movie = 'http://127.0.0.1:8000/api/movies/1/'
endpoint_update_movie = 'http://127.0.0.1:8000/api/movies/1/update/'
endpoint_delete_movie = 'http://127.0.0.1:8000/api/movies/1/delete/'
endpoint_add_genre = 'http://127.0.0.1:8000/api/genres/create/'
endpoint_retrieve_genre = 'http://127.0.0.1:8000/api/genres/1/'
endpoint_update_genre = 'http://127.0.0.1:8000/api/movies/1/genres/'
endpoint_delete_genre = 'http://127.0.0.1:8000/api/genres/delete/'

endpoint_api_view = 'http://127.0.0.1:8000/api/genres/1/movies/'




response = requests.get(endpoint_api_view)

print(response.json())