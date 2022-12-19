from django.db import models

# Create your models here.
class MovieList (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'movie_list'