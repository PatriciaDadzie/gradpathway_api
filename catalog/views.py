
# Create your views here.
from rest_framework import generics
from .models import University, Programme
from .serializers import UniversitySerializer, ProgrammeSerializer

class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class ProgrammeListCreateView(generics.ListCreateAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer


class ProgrammeDetailView(generics.RetrieveAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
