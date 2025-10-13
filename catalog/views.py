from rest_framework import generics, permissions
from .models import University, Programme
from .serializers import UniversitySerializer, ProgrammeSerializer

# Custom permission: Allow read-only access for everyone, write access only for admins
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


# University list & create view
class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAdminOrReadOnly]


# Programme list & create view
class ProgrammeListCreateView(generics.ListCreateAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    permission_classes = [IsAdminOrReadOnly]


# Programme detail view (retrieve only)
class ProgrammeDetailView(generics.RetrieveAPIView):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    permission_classes = [permissions.AllowAny]  
