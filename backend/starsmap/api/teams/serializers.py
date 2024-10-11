from rest_framework import serializers
from django.db.models import Count

from teams.models import Team, Employee
from specialties.models import Grade


# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'


# class TargetEmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TargetEmployee
#         fields = '__all__'


# class EmployeeTeamSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeTeam
#         fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    info_company = serializers.SerializerMethodField()
    great = serializers.SerializerMethodField()
    max_great = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'

    def get_info_company(self, obj):
        employee= Employee.objects.filter(team=obj)
        total_team = len(employee)
        bas_factors = len(employee.filter(bus_factor=True))
        key_people = len(employee.filter(key=True))
        education_request = len(employee.filter(
            employee_skill__education_request=True
        ))
        education_in_progress = len(set(employee.filter(
            employee_check__education_progress=True
        )))
        return {
            'total_team': total_team,
            'bas_factors': bas_factors,
            'key_people': key_people,
            'education_request': education_request,
            'education_in_progress': education_in_progress,
        }

    def get_great(self, obj):
        grades = Grade.objects.filter(employee__team=obj)
        return grades.values('name').annotate(Count('id'))

    def get_max_great(self, obj):
        grades = Grade.objects.filter(employee__team=obj)
        max_grades = round(len(grades.filter(name='Senior'))
                           / len(grades) * 100)
        min_grades = 100 - max_grades
        return {'max_grades': max_grades, 'min_grades': min_grades}


# class RequestTrainingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RequestTraining
#         fields = '__all__'


# class LevelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Level
#         fields = '__all__'
