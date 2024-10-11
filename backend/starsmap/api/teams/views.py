# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
# from rest_framework.filters import OrderingFilter

from teams.models import Team
from .serializers import TeamSerializer
# from .serializers import (EmployeeSerializer, EmployeeTeamSerializer,
#                           LevelSerializer, RequestTrainingSerializer,
#                           TargetEmployeeSerializer, TeamSerializer)


# class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_fields = []
#     ordering_fields = []


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# class TargetEmployeeViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = TargetEmployee.objects.all()
#     serializer_class = TargetEmployeeSerializer


# class EmployeeTeamViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = EmployeeTeam.objects.all()
#     serializer_class = EmployeeTeamSerializer


# class RequestTrainingViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = RequestTraining.objects.all()
#     serializer_class = RequestTrainingSerializer


# class LevelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Level.objects.all()
#     serializer_class = LevelSerializer
