from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic import ListView


from .models import Artist

class ArtistDetailView(DetailView):
	model = Artist

	def get_template_names(self):
		return 'artists.html'

class ArtistListView(ListView):
	model = Artist
	context_object_name = 'artists'
	template_name = 'artists.html'
	
from rest_framework import routers, serializers, viewsets

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = ('id','first_name', 'last_name', 'biography', 'favorite_songs')

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class =  ArtistSerializer
    paginate_by = 1