from django.contrib import admin
from django.urls import path
from .views import UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update/', UserView.as_view({'patch': 'update'})),
    path('me/', UserView.as_view({'get': 'me'}))
]
