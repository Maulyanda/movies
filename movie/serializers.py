from rest_framework import serializers
from movie.models import MovieList

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = '__all__'