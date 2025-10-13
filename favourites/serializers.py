from rest_framework import serializers
from .models import Favourite
from catalog.serializers import ProgrammeSerializer

class FavouriteSerializer(serializers.ModelSerializer):
    programme = ProgrammeSerializer(read_only=True)

    class Meta:
        model = Favourite
        fields = "__all__"
        read_only_fields = ("user", "created_at")
