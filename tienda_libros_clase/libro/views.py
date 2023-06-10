from rest_framework import generics
from .models import Libro
from .serializers import LibroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
class LibroRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

@api_view(['GET'])
def api_libros(request):
    instance = Libro.objects.all().order_by('?').first()

    data = {}
    if instance:
        data = LibroSerializer(instance).data
    return Response(data)
