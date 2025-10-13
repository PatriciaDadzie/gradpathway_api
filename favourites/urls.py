from django.urls import path
from .views import FavouriteListCreateView, FavouriteDeleteView

urlpatterns = [
    path("", FavouriteListCreateView.as_view(), name="favourite-list-create"),
    path("<int:pk>/", FavouriteDeleteView.as_view(), name="favourite-delete"),
]
