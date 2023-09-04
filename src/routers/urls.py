from django.urls import path
from django.urls import include

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

from src.apps.user import views
from src.apps.patient.views.patient_views import (
    PatientViewSet,
    StatusListView,
)
from src.apps.patient.views.record_views import (
    PatientRecordViewSet,
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'status', StatusListView, basename='status')
router.register(r'records', PatientRecordViewSet, basename='record')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', views.RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('roles/', views.RoleListView.as_view()),
    path('me/', views.Profile.as_view()),
]
