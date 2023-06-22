from django.test import TestCase
from rest_framework.test import APIClient
from .models import Genre, Movie

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


#verifica el funcionamiento de la vista MovieListCreateAPIView (listar y crear películas)
class MovieAPITests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        self.genre1 = Genre.objects.create(name='Test Genre1')
        self.genre2 = Genre.objects.create(name='Test Genre2')
        self.movie1 = Movie.objects.create(title='Existing Movie1', genre=self.genre1.name, year=1991)
        self.movie2 = Movie.objects.create(title='Existing Movie2', genre=self.genre2.name, year=1991)
        self.movie3 = Movie.objects.create(title='Existing Movie3', genre=self.genre1.name, year=1991)

    def test_movie_list_create_api_view(self):
        url = f'/api/movies/create/'
        admin_token, _ = Token.objects.get_or_create(user=self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {admin_token.key}')
         # Solicitud POST para crear una película
        movie_data = {
            'title': 'New Movie',
            'genre': self.genre1.name,
            'year': 2023
        }
        response = self.client.post(url, data=movie_data)
        self.assertEqual(response.status_code, 201)

        # Solicitud GET para listar las películas
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)  # Verifica la cantidad de películas devueltas

        #verifica MovieRetrieveAPIView que que obtiene los detalles de una película específica

    def test_movie_retrieve_api_view(self):
        
        url = f'/api/movies/{self.movie1.pk}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Existing Movie1')

    #verifica api_genre_movies, que devuelve las películas de un género específico

    def test_api_genre_movies(self):
        url = f'/api/genres/{self.genre1.pk}/movies/'    
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['genre'], 'Test Genre1')  
        
