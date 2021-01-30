from django.contrib import admin
from .models import Video, YT

class YTAdmin(admin.ModelAdmin):
	yt_display = ["title", "url", "youtube_id", "video"]


admin.site.register(Video)
admin.site.register(YT, YTAdmin)
