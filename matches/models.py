from django.db import models
from django.conf import settings
from transcripts.models import Transcript
from catalog.models import Programme

# Create your models here.from django.db import models


class MatchRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="match_requests")
    transcript = models.ForeignKey(Transcript, on_delete=models.CASCADE)
    filters = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MatchRequest by {self.user.username}"


class MatchResult(models.Model):
    match_request = models.ForeignKey(MatchRequest, on_delete=models.CASCADE, related_name="results")
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    score = models.FloatField()
    reasoning = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.programme.title} ({self.score})"

