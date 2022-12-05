from django.urls import path, include

from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
            TokenObtainPairView,
            TokenRefreshView,
)

from . import views


app_name = 'api_v1'

router = SimpleRouter()

router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
