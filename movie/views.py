from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status

from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse

from movie.models import MovieList
from movie.serializers import MovieListSerializer

from rest_framework.exceptions import NotFound, PermissionDenied

from rest_framework.decorators import action

import json


# Create your views here.
class MoviesList(APIView):
    def get(self, request):
        
        movie = MovieList.objects.all()
        serializer = MovieListSerializer(movie, many=True)

        if len(serializer.data) > 0:
            return Response(serializer.data)
        
        raise NotFound(detail="List Movie not found!", code=400)
    
    def post(self, request):            
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'code': 200,
                'success': 'Data movie berhasil ditambahkan.'
            }, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=400)

class MoviesDetail(APIView):
    def get_object(self, id):
        try:
            return MovieList.objects.get(id=id)
        except MovieList.DoesNotExist:
            raise NotFound(detail="Movie not found!", code=400)
    
    def get(self, request, id, format=None):
        data = self.get_object(id)

        movie = MovieList.objects.filter(id=data.id)
        serializer = MovieListSerializer(movie, many=True)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = MovieListSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):

        data = self.get_object(id)
        data.delete()

        return Response({
                'message': 'Movie berhasil dihapus!'
            }, status=200)