from django.urls import path
from .views import MoviesDetail, MoviesList

urlpatterns = [
    path('movies', MoviesList.as_view()),
    path('movies/<int:id>', MoviesDetail.as_view()),
]