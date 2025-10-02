from rest_framework import serializers
from .models import University, Programme

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"



