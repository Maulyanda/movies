from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoviesDetail, MoviesList

urlpatterns = [
    path('movies', MoviesList.as_view()),
    path('movies/<int:id>', MoviesDetail.as_view()),
]