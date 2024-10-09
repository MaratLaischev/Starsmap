from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from specialties.models import Level, RequestTraining, Skill

from .models import Employee, Team
from .serializers import (EmployeeSerializer, LevelSerializer,
                          RequestTrainingSerializer, SkillSerializer,
                          SpecialityDataSerializer, TeamSerializer)


class EmployeeViewSet(viewsets.ModelViewSet):
    """ViewSet для сотрудников."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet для команд."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SkillViewSet(viewsets.ModelViewSet):
    """ViewSet для навыков."""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class LevelViewSet(viewsets.ModelViewSet):
    """ViewSet для уровней навыков."""
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class RequestTrainingViewSet(viewsets.ModelViewSet):
    """ViewSet для запросов на обучение."""
    queryset = RequestTraining.objects.all()
    serializer_class = RequestTrainingSerializer


class SpecialityDataView(APIView):
    """Представление для вывода данных о специальностях по грейдам."""

    def get(self, request):
        serializer = SpecialityDataSerializer()
        return Response(serializer.data)
