from django.contrib import admin
from artists.models import Artist
from tracks.models import Track
from albums.models import Album

# Register your models here.

class TrackInline(admin.StackedInline):
	model = Track
	extra = 1

class albumInline(admin.StackedInline):
	model = Album
	extra = 1

class ArtistAdmin(admin.ModelAdmin):
	search_fields = ('first_name', 'last_name')
	# filter_horizontal = ('favorite_songs',)
	filter_vertical = ('favorite_songs',)
	inlines 	  = [TrackInline, albumInline] 

admin.site.register(Artist, ArtistAdmin)