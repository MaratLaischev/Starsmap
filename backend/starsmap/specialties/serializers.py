from rest_framework import serializers

from .models import Competence, Grade, Position, RequirementPosition, Skill
from teams.models import Employee


class GradeDataSerializer(serializers.Serializer):
    """Сериализатор для вывода грейдов в формате {name: '', value: ''}."""
    name = serializers.CharField()
    value = serializers.IntegerField()

    class Meta:
        model = Grade
        fields = '__all__'


class GradeSerializer(serializers.Serializer):
    """Кастомный сериализатор для подсчета количества сотрудников по грейдам."""

    def to_representation(self, instance):
        """Группировка грейдов и подсчет сотрудников."""
        employees = Employee.objects.values('grade').annotate(
            count=models.Count('id'))
        grade_data = [{"name": employee['grade'],
                       "value": employee['count']} for employee in employees]
        return grade_data


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'


class RequirementPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementPosition
        fields = '__all__'
