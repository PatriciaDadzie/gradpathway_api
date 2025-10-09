from rest_framework import serializers
from .models import MatchRequest, MatchResult
from catalog.serializers import ProgrammeSerializer

class MatchResultSerializer(serializers.ModelSerializer):
    programme = ProgrammeSerializer(read_only=True)

    class Meta:
        model = MatchResult
        fields = "__all__"


class MatchRequestSerializer(serializers.ModelSerializer):
    results = MatchResultSerializer(many=True, read_only=True)

    class Meta:
        model = MatchRequest
        fields = "__all__"
        read_only_fields = ("user", "created_at", "results")
