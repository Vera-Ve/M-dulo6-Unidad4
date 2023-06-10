import requests

endpoint = 'http://127.0.0.1:8000/libro/1'

endpoint_add = 'http://127.0.0.1:8000/api/movies/create'
endpoint_api_view = 'http://127.0.0.1:8000/libro'

response = requests.get(endpoint_api_view)

print(response.json())