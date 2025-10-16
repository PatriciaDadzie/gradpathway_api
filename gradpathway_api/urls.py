"""
URL configuration for gradpathway_api project.

The `urlpatterns` list routes URLs to views.
For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="GradPathway API",
        default_version='v1',
        description=(
            "API documentation for GradPathway – A platform that helps international students "
            "discover suitable master's programmes worldwide."
        ),
        contact=openapi.Contact(email="support@gradpathway.com"),
    ),
    public=True,  
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core API routes
    path("api/auth/", include("accounts.urls")),
    path("api/catalog/", include("catalog.urls")),
    path("api/transcripts/", include("transcripts.urls")),
    path("api/matches/", include("matches.urls")),
    path("api/favourites/", include("favourites.urls")),

    # API documentation routes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
