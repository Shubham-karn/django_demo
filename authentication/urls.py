from django.urls import path
from .views import register_view, login_view, logout_view
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]