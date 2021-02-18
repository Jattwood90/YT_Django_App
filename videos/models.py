from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        
        verbose_name = "Channel Name"

    def __str__(self):
        return self.title


class YT(models.Model):
    
    title = models.CharField(max_length=255, verbose_name="YouTube Title")
    url = models.URLField(verbose_name="URL")
    youtube_id = models.CharField(max_length=255, verbose_name="YouTube ID")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, default=Video, verbose_name="Channel Name")
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name="Created on")
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name="Updated on")

    class Meta:
        
        ordering = ("-created_at", "title")
        verbose_name = "YouTube Video"
        


    def __str__(self):
        return self.title + ', Youtube ID: ' + self.youtube_id