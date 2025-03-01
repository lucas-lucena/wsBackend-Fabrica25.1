from app_rotten_potatoes.api.viewsets import MovieViewSet, ReviewViewSet
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_rotten_potatoes.api.urls')),
]
