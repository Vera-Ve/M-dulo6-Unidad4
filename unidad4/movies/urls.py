from django.urls import path

from . import views
from .views import MovieViewSet
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('movies_viewset', MovieViewSet)

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('genres/<int:genre_id>/movies/', views.api_genre_movies),
    path('movies/create/', views.MovieListCreateAPIView.as_view()),
    path('movies/<int:pk>/', views.MovieRetrieveAPIView.as_view()),
    path('movies/<int:pk>/update/', views.MovieUpdateAPIView.as_view()),
    path('movies/<int:pk>/delete/', views.MovieDestroyAPIView.as_view()),
    path('genres/create/', views.GenreListCreateAPIView.as_view()),
    path('genres/<int:pk>/', views.GenreRetrieveAPIView.as_view()),
    path('genres/<int:pk>/update/', views.GenreUpdateAPIView.as_view()),
    path('genres/<int:pk>/delete/', views.GenreDestroyAPIView.as_view()),
    path('movies/<int:pk>/delete/', views.GenreDestroyAPIView.as_view()),
] + router.urls