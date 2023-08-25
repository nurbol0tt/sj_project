from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from src.apps.patient.views import PatientViewSet
from rest_framework.routers import DefaultRouter
from src.apps.user import views
from django.urls import include


router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', views.RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('roles/', views.RoleListView.as_view()),
    path('me/', views.Profile.as_view()),
]
