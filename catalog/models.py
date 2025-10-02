from django.db import models


# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Programme(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="programmes")
    title = models.CharField(max_length=255)
    discipline = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration_months = models.IntegerField()
    tuition = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    min_gpa = models.FloatField()
    mode = models.CharField(max_length=20, choices=[("online", "Online"), ("on-campus", "On-Campus")])
    application_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.university.name})"

