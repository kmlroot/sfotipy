from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic import ListView

from albums.models import Album
from artists.models import Artist

class JsonResponseMixin(object):
	def response_handler(self):
		format = self.request.GET.get('format', None)

		if format == 'json':
			return self.json_to_response()

		context = self.get_context_data()
		return self.render_to_response(context)

	def json_to_response(self):
		data = self.get_data()
		return JsonResponse(data, safe=False)
		
class ArtistDetailView(DetailView):
	model = Artist

	def get_template_names(self):
		return 'artists.html'
	

class ArtistListView(ListView):
	model = Artist
	context_object_name = 'artists'
	template_name = 'artists.html'

class AlbumListView(JsonResponseMixin, ListView):
	model = Album
	context_object_name = 'albums'
	template_name = 'albums.html'

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		return self.response_handler()

	def get_data(self):
		data = [{
			'cover': album.cover.url,
			'title': album.title,
			'artist': album.artist.first_name,
		} for album in self.object_list]

		return data

	# def json_to_response(self):
	# 	data = list()
	# 	# for album in self.object_list:
	# 	# 	data.append({
	# 	# 		'cover': album.cover.url,
	# 	# 		'title': album.title,
	# 	# 		'artist': album.artist.first_name,
	# 	# 	})


	# 	return JsonResponse(data, safe=False)

	def get_queryset(self):
		if self.kwargs.get('artist'):
			queryset = self.model.objects.filter(artist__first_name__contains=self.kwargs['artist'])
			# queryset = Album.objects.filter(artist_slug=self.kwargs['artist'])
		else:
			queryset = super(AlbumListView, self).get_queryset()

		return queryset
	
from rest_framework import routers, serializers, viewsets

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = ('id','first_name', 'last_name', 'biography', 'favorite_songs')

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class =  ArtistSerializer
    paginate_by = 1