from django.shortcuts import render

# Create your views here.

from .models import Album

from rest_framework import routers, serializers, viewsets

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'cover', 'artist')

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class =  AlbumSerializer