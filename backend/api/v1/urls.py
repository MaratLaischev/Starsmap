from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet,
    LevelViewSet,
    RequestTrainingViewSet,
    SkillViewSet,
    SpecialityDataViewSet,
    TeamViewSet,
    GradeDataViewSet,
    CompetenceViewSet,
    PositionViewSet,
    RequirementPositionViewSet,
)

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"teams", TeamViewSet)
router.register(r"skills", SkillViewSet)
router.register(r"levels", LevelViewSet)
router.register(r"trainings", RequestTrainingViewSet)
router.register(r"grades", GradeDataViewSet, basename="grades")
router.register(r"specialities", SpecialityDataViewSet, basename="specialities")
router.register(r"competences", CompetenceViewSet, basename="competences")
router.register(r"positions", PositionViewSet, basename="positions")
router.register(
    r"requirementpositions", RequirementPositionViewSet, basename="requirementpositions"
)

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/", include(router.urls)),
]
