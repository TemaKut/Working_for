from django.urls import path, include

from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
            TokenObtainPairView,
            TokenRefreshView,
)

from . import views


app_name = 'api_v1'

router_v1 = SimpleRouter()

router_v1.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('v1/users/me/', views.get_info_about_me, name='users_me'),
    path('v1/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('v1/', include(router_v1.urls)),
]
