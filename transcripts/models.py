from django.db import models
from django.conf import settings


# Create your models here.
class Transcript(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transcripts")
    uploaded_file = models.FileField(upload_to="transcripts/", blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)
    degree_class = models.CharField(max_length=100, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Transcript ({self.gpa or 'N/A'})"
