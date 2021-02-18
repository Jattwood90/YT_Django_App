from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Video, YT
from import_export import resources
from django.contrib.admin.models import LogEntry


@admin.register(YT)
class YTAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ("title", "video", "youtube_id", "created_at")
	list_filter = ('video',)

	LogEntry.objects.all().delete()
	

	class Media:
		css = {
			'all': ('/templates/admin/admin-extra.css',)
		}

admin.site.register(Video)

