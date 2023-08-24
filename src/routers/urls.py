from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from src.apps.user import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('roles/', views.RoleListView.as_view()),
    path('me/', views.Profile.as_view()),
]
