from rest_framework import serializers

from .models import (Employee, EmployeeTeam, Level, RequestTraining,
                     TargetEmployee, Team)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TargetEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetEmployee
        fields = '__all__'


class EmployeeTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTeam
        fields = '__all__'


class RequestTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTraining
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
