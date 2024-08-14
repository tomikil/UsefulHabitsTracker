from django.urls import path

from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.permissions import AllowAny

from users.views import UserCreateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('register/', UserCreateAPIView.as_view(permission_classes=(AllowAny, )), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
