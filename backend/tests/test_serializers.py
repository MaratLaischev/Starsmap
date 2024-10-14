from django.test import TestCase
from core.models import (
    Competence, Employee, Grade, Level, Position, RequestTraining,
    RequirementPosition, Skill, Team
)
from api.v1.serializers import (
    GradeSerializer, SkillSerializer, PositionSerializer,
    CompetenceSerializer, RequirementPositionSerializer, TeamSerializer,
    EmployeeSerializer, LevelSerializer, RequestTrainingSerializer,
    SpecialityDataSerializer  # Add this import
)
from django.contrib.auth import get_user_model
from django.db import models
from datetime import date

User = get_user_model()


class SkillSerializerTest(TestCase):
    def test_skill_serializer(self):
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        serializer = SkillSerializer(skill)
        self.assertEqual(serializer.data['skill_name'], "Test Skill")
        self.assertEqual(serializer.data['skill_competence_name'], "Test Competence")


class PositionSerializerTest(TestCase):
    def test_position_serializer(self):
        position = Position.objects.create(name="Test Position")
        serializer = PositionSerializer(position)
        self.assertEqual(serializer.data['name'], "Test Position")


class CompetenceSerializerTest(TestCase):
    def test_competence_serializer(self):
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        serializer = CompetenceSerializer(competence)
        self.assertEqual(serializer.data['name'], "Test Competence")
        self.assertEqual(serializer.data['type'], "Soft")


class RequirementPositionSerializerTest(TestCase):
    def test_requirement_position_serializer(self):
        position = Position.objects.create(name="Test Position")
        grade = Grade.objects.create(grade="Junior")
        skill = Skill.objects.create(name="Test Skill", competence=Competence.objects.create(name="Test Competence", type="Soft"), domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        requirement_position = RequirementPosition.objects.create(position=position, grade=grade, skill=skill, rating=5)
        serializer = RequirementPositionSerializer(requirement_position)
        self.assertEqual(serializer.data['rating'], 5)


class TeamSerializerTest(TestCase):
    def test_team_serializer(self):
        team = Team.objects.create(name="Test Team")
        serializer = TeamSerializer(team)
        self.assertEqual(serializer.data['name'], "Test Team")

class SpecialityDataSerializerTest(TestCase):
    def test_speciality_data_serializer(self):
        data = {'key': 'value'}
        serializer = SpecialityDataSerializer(data)
        self.assertEqual(serializer.data, data)


class EmployeeSerializerTest(TestCase):
    def test_employee_serializer(self):
        team = Team.objects.create(name="Test Team")
        position = Position.objects.create(name="Test Position")
        grade = Grade.objects.create(grade="Junior")
        employee = Employee.objects.create(
            name_surname="Test Employee", position=position, team=team, grade=grade,
            bus_factor=True, key=True
        )
        skill = Skill.objects.create(
            name="Test Skill", competence=Competence.objects.create(name="Test Competence", type="Soft"),
            domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True,
            key=True, education_request=False, education_in_progress=False
        )
        employee.skills.add(skill)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(serializer.data['employee_name_surname'], "Test Employee")
        self.assertEqual(serializer.data['employee_position_name'], "Test Position")
        self.assertEqual(serializer.data['employee_team_name'], "Test Team")
        self.assertEqual(serializer.data['employee_grade_name'], "Junior")
        self.assertEqual(serializer.data['employee_bus_factor'], True)
        self.assertEqual(serializer.data['employee_key'], True)
        self.assertEqual(serializer.data['skills'][0]['skill_name'], "Test Skill")
