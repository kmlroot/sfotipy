from django.shortcuts import render

# Create your views here.

from .models import Album
from .models import Artist
from artists.views import JsonResponseMixin
from django.views.generic import ListView, DetailView

from rest_framework import routers, serializers, viewsets

class AlbumDetailView(JsonResponseMixin, DetailView):
	model = Album
	template_name = 'album_detail.html'
	slug_url_kwarg = 'artist_id'
	slug_field = 'artist_id'
	
	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		return self.response_handler()
		
		# format = self.request.GET.get('format', None)
		# if format == 'json':
		# 	return self.json_to_response()

		# context = self.get_context_data(object=self.object)
		# return self.render_to_response(context)

	def get_data(self):
		data = {
			'album': {
				'cover': self.object.cover.url,
				'title': self.object.title,
				'artist': self.object.artist.first_name,
				'tracks': [t.title for t in self.object.track_set.all()]
			}
		}
		# return JsonResponse(data, safe=False)
		return data

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'cover', 'artist')

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class =  AlbumSerializer