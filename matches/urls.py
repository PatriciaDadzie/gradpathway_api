from django.urls import path
from .views import MatchRequestListCreateView

urlpatterns = [
    path("", MatchRequestListCreateView.as_view(), name="match-list-create"),
]
