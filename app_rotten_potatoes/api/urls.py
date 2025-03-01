from django.urls import path, include
from .viewsets import MovieViewSet, ReviewViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('movies/', MovieViewSet.as_view({
        'get': 'list'
    })),
    path('movies/create/', MovieViewSet.as_view({
        'post': 'create'
    })),
    path('movies/<str:pk>/', MovieViewSet.as_view({
        'get': 'retrieve',
    })),
    path('movies/<str:pk>/update/', MovieViewSet.as_view({
        'put': 'update',
    })),
    path('movies/<str:pl>/delete/', MovieViewSet.as_view({
        'delete': 'destroy',
    })),
    path('reviews/', ReviewViewSet.as_view({
        'get': 'list'
    })),
    path('reviews/create/', ReviewViewSet.as_view({
        'post': 'create'
    })),
    path('reviews/<str:pk>/', ReviewViewSet.as_view({
        'get': 'retrieve',
    })),
    path('reviews/<str:pk>/update/', ReviewViewSet.as_view({
        'put': 'update',
    })),
    path('reviews/<str:pk>/delete/', ReviewViewSet.as_view({
        'delete': 'destroy',
    })),
]