from os import name
from django.urls import path
from base.views import user_views as views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.getUsers, name="users"),
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path("register/", views.registerUser, name="register-users"),
    path("profile/", views.getUsersProfile, name="users-profile"),
]
