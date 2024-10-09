from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Competence, Position, RequirementPosition, Skill
from .serializers import (CompetenceSerializer, GradeSerializer,
                          PositionSerializer, RequirementPositionSerializer,
                          SkillSerializer)


class GradeDataView(APIView):
    """Представление для вывода данных о грейдах."""

    def get(self, request):
        serializer = GradeSerializer()
        return Response(serializer.data)


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
