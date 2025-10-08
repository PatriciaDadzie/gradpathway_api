from rest_framework import generics, permissions
from .models import Transcript
from .serializers import TranscriptSerializer

class TranscriptListCreateView(generics.ListCreateAPIView):
    serializer_class = TranscriptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transcript.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
