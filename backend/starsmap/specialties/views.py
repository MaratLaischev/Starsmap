from rest_framework import viewsets

from .models import Competence, Grade, Position, RequirementPosition, Skill
from .serializers import (CompetenceSerializer, GradeSerializer,
                          PositionSerializer, RequirementPositionSerializer,
                          SkillSerializer)


class GradeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


class RequirementPositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RequirementPosition.objects.all()
    serializer_class = RequirementPositionSerializer
