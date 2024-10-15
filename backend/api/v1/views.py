from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from core.models import (
    Competence,
    Employee,
    Level,
    Position,
    RequestTraining,
    RequirementPosition,
    Skill,
    Team,
)
from .serializers import (
    CompetenceSerializer,
    EmployeeSerializer,
    GradeSerializer,
    LevelSerializer,
    PositionSerializer,
    RequestTrainingSerializer,
    RequirementPositionSerializer,
    SkillSerializer,
    SpecialityDataSerializer,
    TeamSerializer,
)


class GradeDataViewSet(viewsets.ViewSet):
    """Представление для модели Grade."""

    serializer_class = GradeSerializer

    def list(self, request):
        cache_key = "grade_data"
        serializer_data = cache.get(cache_key)
        if not serializer_data:
            serializer = GradeSerializer()
            serializer_data = serializer.data
            cache.set(cache_key, serializer_data, 60 * 15)
        return Response(serializer_data)


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели Skill."""

    queryset = Skill.objects.select_related("competence").all()
    serializer_class = SkillSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "skill_data"
        response_data = cache.get(cache_key)
        if not response_data:
            response = super().list(request, *args, **kwargs)
            response_data = response.data
            cache.set(cache_key, response_data, 60 * 15)
        return Response(response_data)


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели Position."""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "position_data"
        response_data = cache.get(cache_key)
        if not response_data:
            response = super().list(request, *args, **kwargs)
            response_data = response.data
            cache.set(cache_key, response_data, 60 * 15)
        return Response(response_data)


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели Competence."""

    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "competence_data"
        response_data = cache.get(cache_key)
        if not response_data:
            response = super().list(request, *args, **kwargs)
            response_data = response.data
            cache.set(cache_key, response_data, 60 * 15)
        return Response(response_data)


class RequirementPositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели RequirementPosition."""

    queryset = RequirementPosition.objects.select_related(
        "position", "grade", "skill"
    ).all()
    serializer_class = RequirementPositionSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "requirement_position_data"
        response_data = cache.get(cache_key)
        if not response_data:
            response = super().list(request, *args, **kwargs)
            response_data = response.data
            cache.set(cache_key, response_data, 60 * 15)  # Cache for 15 minutes
        return Response(response_data)


class EmployeeViewSet(viewsets.ModelViewSet):
    """Представление для модели Employee."""

    queryset = (
        Employee.objects.select_related("team")
        .prefetch_related("skills__competence")
        .all()
    )
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "employee_data"
        response_data = cache.get(cache_key)
        if not response_data:
            response = super().list(request, *args, **kwargs)
            response_data = response.data
            cache.set(cache_key, response_data, 60 * 15)
        return Response(response_data)


class TeamViewSet(viewsets.ModelViewSet):
    """Представление для модели Team."""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "team_data"
        response_data = cache.get(cache_key)
        if not response_data:
            response = super().list(request, *args, **kwargs)
            response_data = response.data
            cache.set(cache_key, response_data, 60 * 15)
        return Response(response_data)


class LevelViewSet(viewsets.ModelViewSet):
    """Представление для модели Level."""

    queryset = Level.objects.select_related("employee", "skill__competence").all()
    serializer_class = LevelSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "level_data"
        response_data = cache.get(cache_key)
        if not response_data:
            response = super().list(request, *args, **kwargs)
            response_data = response.data
            cache.set(cache_key, response_data, 60 * 15)
        return Response(response_data)


class RequestTrainingViewSet(viewsets.ModelViewSet):
    """Представление для модели RequestTraining."""

    queryset = RequestTraining.objects.select_related(
        "employee", "skill__competence"
    ).all()
    serializer_class = RequestTrainingSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "request_training_data"
        response_data = cache.get(cache_key)
        if not response_data:
            response = super().list(request, *args, **kwargs)
            response_data = response.data
            cache.set(cache_key, response_data, 60 * 15)
        return Response(response_data)


class SpecialityDataViewSet(viewsets.ViewSet):
    """Представление для модели SpecialityData."""

    serializer_class = SpecialityDataSerializer

    def list(self, request):
        cache_key = "speciality_data"
        serializer_data = cache.get(cache_key)
        if not serializer_data:
            serializer = SpecialityDataSerializer()
            serializer_data = serializer.data
            cache.set(cache_key, serializer_data, 60 * 15)
        return Response(serializer_data)
