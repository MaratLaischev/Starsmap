from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import (
    Competence, Position, RequirementPosition, Skill, Employee, Team, Level, RequestTraining
)
from .serializers import (
    CompetenceSerializer, GradeSerializer, PositionSerializer, RequirementPositionSerializer,
    SkillSerializer, EmployeeSerializer, LevelSerializer, RequestTrainingSerializer,
    SkillSerializer as TeamSkillSerializer, SpecialityDataSerializer, TeamSerializer
)


class GradeDataViewSet(viewsets.ViewSet):
    """Представление для модели Grade."""

    def list(self, request):
        serializer = GradeSerializer()
        return Response(serializer.data)


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели Skill."""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели Position."""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели Competence."""
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


class RequirementPositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для модели RequirementPosition."""
    queryset = RequirementPosition.objects.all()
    serializer_class = RequirementPositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """Представление для модели Employee."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """Представление для модели Team."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class LevelViewSet(viewsets.ModelViewSet):
    """Представление для модели Level."""
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class RequestTrainingViewSet(viewsets.ModelViewSet):
    """Представление для модели RequestTraining."""
    queryset = RequestTraining.objects.all()
    serializer_class = RequestTrainingSerializer


class SpecialityDataViewSet(viewsets.ViewSet):
    """Представление для модели SpecialityData."""

    def list(self, request):
        serializer = SpecialityDataSerializer()
        return Response(serializer.data)