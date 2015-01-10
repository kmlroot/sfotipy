import json
import time 
from django.shortcuts import render, get_object_or_404
from django.http 	  import HttpResponse, Http404	
from .models 		  import Track	
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from artists.task import demorada

# Create your views here.

# @cache_page(60)
def track_view(request, title):
	# try:
	# 	track = Track.objects.get(title=title)
	# except Track.DoesNotExist:
	# 	raise Http404
	# import ipdb; ipdb.set_trace()
	track = get_object_or_404(Track, title=title)

	# return HttpResponse('El track fue encontrado con exito y su nombre es: ' + title)
	
	bio = track.artist.biography
	# data = cache.get('data_%s' %title)
	data = {
		'title' : 	track.title,
		'order' : 	track.order,
		'album' : 	track.album.title,
		'artist':  	{
			'name'		: track.artist.first_name,
			'biography'	: bio,
		}
	}
	# demorada()
	# demorada.apply_async(countdown=5)
	# cache.set('data_%s' %title, data)
	# time.sleep(5)
	return render(request, 'track.html', {'track': track, 'bio': bio})

	#json_data = json.dumps(data)

	#return HttpResponse(json_data, content_type='application/json')

from rest_framework import routers, serializers, viewsets

class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields = ('title', 'order', 'track_file', 'artist', 'album')

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class =  TrackSerializer