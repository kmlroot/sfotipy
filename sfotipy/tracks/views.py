import json
from django.shortcuts import render, get_object_or_404
from django.http 	  import HttpResponse, Http404	
from .models 		  import Track	

# Create your views here.

def track_view(request, title):
	# try:
	# 	track = Track.objects.get(title=title)
	# except Track.DoesNotExist:
	# 	raise Http404
	# import ipdb; ipdb.set_trace()
	track = get_object_or_404(Track, title=title)

	# return HttpResponse('El track fue encontrado con exito y su nombre es: ' + title)
	
	bio = track.artist.biography

	data = {
		'title' : 	track.title,
		'order' : 	track.order,
		'album' : 	track.album.title,
		'artist':  	{
			'name'		: track.artist.first_name,
			'biography'	: bio,
		}
	}

	return render(request, 'track.html', {'track': track, 'bio': bio})

	#json_data = json.dumps(data)

	#return HttpResponse(json_data, content_type='application/json')