from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class YT(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    youtube_id = models.CharField(max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=False)

    def __str__(self):
        return self.title + ', Youtube ID: ' + self.youtube_id