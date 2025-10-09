
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import MatchRequest
from .serializers import MatchRequestSerializer
from .utils import generate_matches

class MatchRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = MatchRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MatchRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        match_request = serializer.save(user=self.request.user)
        generate_matches(match_request)
