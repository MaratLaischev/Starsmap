from rest_framework import serializers
from django.db import models
from core.models import (
    Competence, Employee, Grade, Level, Position, RequestTraining,
    RequirementPosition, Skill, Team
)


class GradeSerializer(serializers.Serializer):
    """Кастомный сериализатор для подсчета количества сотрудников по грейдам."""

    def to_representation(self, instance):
        """Группировка грейдов и подсчет сотрудников."""
        grades = Grade.objects.annotate(
            count=models.Count('employee')
        ).values('grade', 'count')
        return [{'name': grade['grade'], 'value': grade['count']} for grade in grades]


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Skill."""
    skill_name = serializers.CharField(source='name')
    skill_competence_name = serializers.CharField(source='competence.name')
    skill_domain_name = serializers.CharField(source='domain_name')
    skill_hard_soft_type = serializers.CharField(source='hard_soft_type')
    skill_estimation = serializers.IntegerField(source='estimation')
    skill_accordance = serializers.BooleanField(source='accordance')
    skill_key = serializers.BooleanField(source='key')
    skill_education_request = serializers.BooleanField(source='education_request')
    skill_education_in_progress = serializers.BooleanField(
        source='education_in_progress'
    )

    class Meta:
        model = Skill
        fields = [
            'skill_name', 'skill_competence_name', 'skill_domain_name',
            'skill_hard_soft_type', 'skill_estimation', 'skill_accordance',
            'skill_key', 'skill_education_request', 'skill_education_in_progress'
        ]


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Position."""
    class Meta:
        model = Position
        fields = '__all__'


class CompetenceSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Competence."""
    class Meta:
        model = Competence
        fields = '__all__'


class RequirementPositionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели RequirementPosition."""
    class Meta:
        model = RequirementPosition
        fields = '__all__'


class SpecialityDataSerializer(serializers.Serializer):
    """Сериализатор для группировки специальностей по грейдам."""

    def to_representation(self, instance):
        return instance


class TeamSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Team."""
    class Meta:
        model = Team
        fields = ['name']


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Employee."""
    employee_id = serializers.IntegerField(source='id')
    employee_name_surname = serializers.CharField(source='name_surname')
    employee_position_name = serializers.CharField(source='position')
    employee_team_name = serializers.CharField(source='team.name')
    employee_grade_name = serializers.CharField(source='grade')
    employee_bus_factor = serializers.BooleanField(source='bus_factor')
    employee_key = serializers.BooleanField(source='key')
    skills = SkillSerializer(many=True)

    class Meta:
        model = Employee
        fields = [
            'employee_id', 'employee_name_surname', 'employee_position_name',
            'employee_team_name', 'employee_grade_name', 'employee_bus_factor',
            'employee_key', 'skills'
        ]


class LevelSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Level."""
    skill = SkillSerializer()

    class Meta:
        model = Level
        fields = '__all__'


class RequestTrainingSerializer(serializers.ModelSerializer):
    """Сериализатор для модели RequestTraining."""
    employee = serializers.StringRelatedField()
    skill = SkillSerializer()

    class Meta:
        model = RequestTraining
        fields = '__all__'
