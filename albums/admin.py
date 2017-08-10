from django.contrib import admin

from albums.models import Album
from sorl.thumbnail import get_thumbnail

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'imagen_album')

	def imagen_album(self, obj):
		return '<img src="%s">' % obj.cover.url
		# return '<img src="%s">' % get_thumbnail(obj.cover, '50x50').url 
	imagen_album.allow_tags = True

admin.site.register(Album, AlbumAdmin)