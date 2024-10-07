from rest_framework import serializers
from django.db.models import Count

from .models import (Employee, EmployeeTeam, Level, RequestTraining,
                     TargetEmployee, Team)
from specialties.models import Grade


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TargetEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetEmployee
        fields = '__all__'


class EmployeeTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTeam
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    total_team = serializers.SerializerMethodField()
    bas_factors = serializers.SerializerMethodField()
    request_training = serializers.SerializerMethodField()
    great = serializers.SerializerMethodField()
    max_great = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'

    def get_total_team(self, obj):
        return len(EmployeeTeam.objects.filter(team=obj))

    def get_bas_factors(self, obj):
        return len(Employee.objects.filter(employee_team__team=obj,
                                           bus_factor=True))

    def get_request_training(self, obj):
        return len(RequestTraining.objects.filter(
            employee__employee_team__team=obj
        ))

    def get_great(self, obj):
        grades = Grade.objects.filter(employee__employee_team__team=obj)
        return grades.values('grade').annotate(Count('id'))

    def get_max_great(self, obj):
        grades = Grade.objects.filter(employee__employee_team__team=obj)
        max_grades = round(len(grades.filter(grade='Senior'))
                           / len(grades) * 100)
        min_grades = 100 - max_grades
        return {'max_grades': max_grades, 'min_grades': min_grades}


class RequestTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTraining
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
