from django.urls import include, path
from rest_framework.routers import DefaultRouter
from specialties.views import GradeDataView

from .views import (EmployeeViewSet, LevelViewSet, RequestTrainingViewSet,
                    SkillViewSet, SpecialityDataView, TeamViewSet)

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'trainings', RequestTrainingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('grades/', GradeDataView.as_view(), name='grades'),
    path('specialities/', SpecialityDataView.as_view(), name='specialities'),
]
