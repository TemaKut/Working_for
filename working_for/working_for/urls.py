from django.contrib import admin
from django.urls import path, include

from .settings import DEBUG


urlpatterns = [
    path('api/', include('api.urls', namespace='api_v1')),
    path('admin/', admin.site.urls),
]

# Подключение документации API
if DEBUG:

    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Working_for API",
            default_version='v1',
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path(
            'redoc/',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'
        ),
    ] 
