from .models import Video, YT
from import_export import resources

class YTResource(resources.ModelResource):

	class Meta:
		model = YT
		fields = ("title", "video", "youtube_id", "url", "created_at")	