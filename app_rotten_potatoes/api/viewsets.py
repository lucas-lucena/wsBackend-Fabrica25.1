from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
import requests
from ..models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

# Consuming OMDB API with requests library in Django viewsets
# CRUD operations for Movie model
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request):
        title = request.query_params.get('title', None)
        if title is None:
            return super().list(request)
        
        api_key = 'c31f0ffb'  
        api_url = f"http://www.omdbapi.com/?apikey={api_key}&s={title}"
        response = requests.get(api_url)
        return Response(response.json(), status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        title = request.query_params.get('title', None)
        if title is None:
            return super().retrieve(request, pk)
        
        api_key = 'c31f0ffb'  
        api_url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
        response = requests.get(api_url)
        return Response(response.json(), status=status.HTTP_200_OK)

# CRUD operations for Review model 
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request):
        movie = Movie.objects.get(pk=request.data['movie'])
        if movie is None:
            return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
