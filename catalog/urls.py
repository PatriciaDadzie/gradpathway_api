from django.urls import path
from .views import UniversityListCreateView, ProgrammeListCreateView, ProgrammeDetailView

urlpatterns = [
    path("universities/", UniversityListCreateView.as_view(), name="universities"),
    path("programmes/", ProgrammeListCreateView.as_view(), name="programmes"),
    path("programmes/<int:pk>/", ProgrammeDetailView.as_view(), name="programme-detail"),
]
