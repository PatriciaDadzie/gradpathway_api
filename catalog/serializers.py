from rest_framework import serializers
from .models import University, Programme

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class ProgrammeSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)

    class Meta:
        model = Programme
        fields = "__all__"
