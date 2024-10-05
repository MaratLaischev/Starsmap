from django.urls import include, path
from rest_framework.routers import DefaultRouter
from specialties.views import (CompetenceViewSet, GradeViewSet,
                               PositionViewSet, RequirementPositionViewSet,
                               SkillViewSet)

from .views import (EmployeeTeamViewSet, EmployeeViewSet, LevelViewSet,
                    RequestTrainingViewSet, TargetEmployeeViewSet, TeamViewSet)

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'team', TeamViewSet)
router.register(r'grade', GradeViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'competency', CompetenceViewSet)
router.register(r'requirement-position', RequirementPositionViewSet)
router.register(r'position', PositionViewSet)
router.register(r'target-employee', TargetEmployeeViewSet)
router.register(r'employee-team', EmployeeTeamViewSet)
router.register(r'request-traning', RequestTrainingViewSet)
router.register(r'level', LevelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
