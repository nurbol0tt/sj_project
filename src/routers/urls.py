from django.urls import path
from django.urls import include

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

from src.apps.patient.views.comment_views import (
    DiaryViewSet,
    PsychologicalConsultationViewSet,
    FileViewSet,
)
from src.apps.patient.views.epicrisis_views import EpicrisisViewSet
from src.apps.user import views
from src.apps.patient.views.patient_views import (
    PatientViewSet,
    StatusListView,
)
from src.apps.patient.views.record_views import (
    PatientRecordViewSet,
    MonthlyIncomeViewSet,

)
from src.apps.user.views import StaffViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'status', StatusListView, basename='status')
router.register(r'records', PatientRecordViewSet, basename='record')
router.register(r'diaries', DiaryViewSet, basename='diary')
router.register(r'psychology', PsychologicalConsultationViewSet, basename='psychology')
router.register(r'files', FileViewSet, basename='file')
router.register(r'epicrisis', EpicrisisViewSet, basename='file')
router.register(r'income', MonthlyIncomeViewSet, basename='file')
router.register(r'staffs', StaffViewSet, basename='file')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', views.RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('roles/', views.RoleListView.as_view()),
    path('me/', views.Profile.as_view())
]
