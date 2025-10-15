
from django.db import models
from django.conf import settings
from catalog.models import Programme

# Create your models here.
class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("user", "programme")

    def __str__(self):
        return f"{self.user.username} → {self.programme.title}"
