from django.test import TestCase
from core.models import (
    Competence, Employee, Grade, Level, Position, RequestTraining,
    RequirementPosition, Skill, Team
)
from api.v1.serializers import (
    GradeSerializer, SkillSerializer, PositionSerializer,
    CompetenceSerializer, RequirementPositionSerializer, TeamSerializer,
    EmployeeSerializer, LevelSerializer, RequestTrainingSerializer,
    RegisterSerializer, LoginSerializer
)
from django.contrib.auth import get_user_model
from django.db import models

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

class LevelSerializerTest(TestCase):
    def test_level_serializer(self):
        employee = Employee.objects.create(email="test@example.com", name_surname="Test User")
        skill = Skill.objects.create(name="Test Skill", competence=Competence.objects.create(name="Test Competence", type="Soft"), domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        level = Level.objects.create(employee=employee, skill=skill, data="2023-01-01", evaluation="Test Evaluation", name="Test Level")
        serializer = LevelSerializer(level)
        self.assertEqual(serializer.data['data'], "2023-01-01")


class RequestTrainingSerializerTest(TestCase):
    def test_request_training_serializer(self):
        employee = Employee.objects.create(email="test@example.com", name_surname="Test User")
        skill = Skill.objects.create(name="Test Skill", competence=Competence.objects.create(name="Test Competence", type="Soft"), domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        request_training = RequestTraining.objects.create(employee=employee, skill=skill, desired_result="Test Result", start_date="2023-01-01", end_date="2023-12-31", status="Pending")
        serializer = RequestTrainingSerializer(request_training)
        self.assertEqual(serializer.data['desired_result'], "Test Result")


class RegisterSerializerTest(TestCase):
    def test_register_serializer(self):
        data = {
            'email': 'test@example.com',
            'name_surname': 'Test User',
            'password': 'password123'
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.name_surname, 'Test User')
