from rest_framework import serializers
from .models import Employee, Team
from specialties.models import Skill, Level, RequestTraining


class HardSoftSkillsField(serializers.Field):
    """Кастомное поле для сериализации hard и soft skills."""

    def to_representation(self, value):
        """Преобразование JSON поля в требуемый формат."""
        if isinstance(value, dict):
            return [
                {"item": key, "value": int(val)} for key, val in value.items()]
        return value

    def to_internal_value(self, data):
        """Обратное преобразование для записи данных."""
        if isinstance(data, list):
            return {item["item"]: item["value"] for item in data}
        return data


class SpecialityDataSerializer(serializers.Serializer):
    """Сериализатор для группировки специальностей по грейдам."""

    def to_representation(self, instance):
        """Группировка специальностей по грейдам."""
        result = {}
        employees = Employee.objects.values('grade', 'position').annotate(
            count=models.Count('id'))
        for employee in employees:
            grade = employee['grade'].lower()
            if grade not in result:
                result[grade] = []

            result[grade].append({
                "name": employee['position'],
                "value": employee['count']
            })

        return result


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Skill."""
    competence = serializers.StringRelatedField()

    class Meta:
        model = Skill
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Team."""
    class Meta:
        model = Team
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Employee."""
    team = TeamSerializer()
    hard_skills = HardSoftSkillsField()
    soft_skills = HardSoftSkillsField()

    class Meta:
        model = Employee
        fields = '__all__'


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
