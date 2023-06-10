from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_libros),
    path('<int:pk>', views.LibroRetrieveAPIView.as_view()),
    path('create', views.LibroListCreateAPIView.as_view()),
]