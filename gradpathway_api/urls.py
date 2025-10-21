from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.http import JsonResponse

schema_view = get_schema_view(
    openapi.Info(
        title="GradPathway API",
        default_version='v1',
        description="API documentation for GradPathway- helping international students find graduate programmes.",
        contact=openapi.Contact(email="support@gradpathway.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def home(request):
    return JsonResponse({"message": "Welcome to GradPathway API", "status": "running"})

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    path('api/auth/', include('accounts.urls')),
    path('api/catalog/', include('catalog.urls')),
    path('api/transcripts/', include('transcripts.urls')),
    path('api/matches/', include('matches.urls')),
    path('api/favourites/', include('favourites.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
