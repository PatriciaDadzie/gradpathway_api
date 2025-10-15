from rest_framework import serializers
from .models import Favourite
from catalog.models import Programme
from catalog.serializers import ProgrammeSerializer

class FavouriteSerializer(serializers.ModelSerializer):
    # Show detailed programme info when reading
    programme = ProgrammeSerializer(read_only=True)
    # Accept programme ID when writing
    programme_id = serializers.PrimaryKeyRelatedField(
        queryset=Programme.objects.all(),
        source='programme',
        write_only=True
    )

    class Meta:
        model = Favourite
        fields = ['id', 'user', 'programme', 'programme_id', 'created_at']
        read_only_fields = ('user', 'created_at')
