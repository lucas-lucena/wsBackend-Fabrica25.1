from rest_framework import viewsets, status
from rest_framework.response import Response
import requests
from ..models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from . import utils


# Consuming OMDB API with requests library in Django viewsets
# CRUD operations for Movie model
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request):
        title = request.data.get('title')

        data = utils.search_movie(title, requests)
        if data.get('Response') == 'False':
                return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        utils.save_movie(data)
        return Response(data, status=status.HTTP_201_CREATED)


    def list(self, request):
        title = request.query_params.get('title')
        if title is None:
            return super().list(request)

        data = utils.search_movie(title, requests)
        return Response(data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        title = request.query_params.get('title')
        if title is None:
            return super().retrieve(request, pk)

        data = utils.search_movie(title, requests)
        return Response(data, status=status.HTTP_200_OK)


    def update(self, request, pk=None):
        movie = self.get_object()
        title = request.data.get('title')
        data = utils.search_movie(title, requests)
        if data.get('Response') == 'False':
            return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        movie.imdb_rating = data.get('imdbRating')
        movie.save()
        return Response(data, status=status.HTTP_200_OK)


    def destroy(self, request, pk=None):
        movie = self.get_object()
        movie.delete()
        return Response({'message': 'Movie deleted'}, status=status.HTTP_204_NO_CONTENT)
    

# CRUD operations for Review model 
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request):
        movie_id = request.data.get('movie')
        if movie_id is None:
            return Response({'message': 'Movie ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            movie = Movie.objects.get(pk=movie_id)
            review = Review(movie=movie, movie_title=movie.title, review_rating=request.data.get('review_rating'), body=request.data.get('body'))
        except Movie.DoesNotExist:
            movie_title = request.data.get('title')
            if not movie_title:
                return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        review.save()
        return Response({'message': 'Review created'}, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        movie = request.query_params.get('movie', None)
        if movie is None:
            return super().list(request)
        
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        movie = request.query_params.get('movie', None)
        if movie is None:
            return super().retrieve(request, pk)
        
        review = Review.objects.get(movie=movie, pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        review = self.get_object()
        review.review_rating = request.data.get('review_rating')
        review.body = request.data.get('body')
        review.save()
        return Response({'message': 'Review updated'}, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        review = self.get_object()
        review.delete()
        return Response({'message': 'Review deleted'}, status=status.HTTP_204_NO_CONTENT)

