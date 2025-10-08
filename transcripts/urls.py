from django.urls import path
from .views import TranscriptListCreateView

urlpatterns = [
    path("", TranscriptListCreateView.as_view(), name="transcript-list-create"),
]
