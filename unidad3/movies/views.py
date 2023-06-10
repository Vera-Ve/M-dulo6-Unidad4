from rest_framework import generics
from .models import Genre, Movie
from .serializer import GenreSerializer, MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Vista genérica para crear una nueva película y listar películas
class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Vista genérica para obtener los detalles de una película
class MovieRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Vista genérica para actualizar una película existente
class MovieUpdateAPIView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Vista genérica para eliminar una película
class MovieDestroyAPIView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Vista genérica para crear nuevg genero de película  y listar generos
class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# Vista genérica para obtener los detalles de un género
class GenreRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# Vista genérica para actualizar un género existente
class GenreUpdateAPIView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# Vista genérica para eliminar un género
class GenreDestroyAPIView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@api_view(['GET'])
def api_genre_movies(request, genre_id):
    instanceGenre = Genre.objects.filter(pk=genre_id).first()

    data = {}
    if instanceGenre:
        instanceMovies = Movie.objects.filter(genre=instanceGenre.name)
        data = {
            'genre': instanceGenre.name,
            'movies': [movie.title for movie in instanceMovies]
        }
    print('instanceGenre:', instanceGenre)
    print('instanceMovies:', instanceMovies)
    print('data:', data)
    return Response(data)