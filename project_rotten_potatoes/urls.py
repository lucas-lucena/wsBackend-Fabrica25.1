"""
URL configuration for project_rotten_potatoes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app_rotten_potatoes.api.viewsets import MovieViewSet, ReviewViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin

route = DefaultRouter()
route.register(r'movies', MovieViewSet)
route.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
]
