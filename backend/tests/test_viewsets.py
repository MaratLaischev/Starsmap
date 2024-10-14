from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from core.models import (
    Competence, Employee, Grade, Level, Position, RequestTraining,
    RequirementPosition, Skill, Team
)
from django.urls import reverse
from django.contrib.auth import get_user_model
from io import StringIO
from django.core.management import call_command

User = get_user_model()

class GradeDataViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('grades-list')

    def test_list_grades(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SkillViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('skill-list')

    def test_list_skills(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PositionViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('positions-list')

    def test_list_positions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CompetenceViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('competences-list')

    def test_list_competences(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class RequirementPositionViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('requirementpositions-list')

    def test_list_requirement_positions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class EmployeeViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('employee-list')
        self.team = Team.objects.create(name='Test Team')
        self.employee_data = {
            'email': 'test@example.com',
            'name_surname': 'Test User',
            'position': 'Developer',
            'team': self.team.id,
            'grade': 'Junior',
            'bus_factor': False,
            'key': False
        }

    def test_list_employees(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('team-list')
        self.team_data = {'name': 'Test Team'}

    def test_create_team(self):
        response = self.client.post(self.url, self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_teams(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SpecialityDataViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('specialities-list')

    def test_list_specialities(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register')
        self.user_data = {
            'email': 'test@example.com',
            'name_surname': 'Test User',
            'password': 'password123'
        }

    def test_register_user(self):
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ImportDataCommandTest(TestCase):
    def test_import_data(self):
        out = StringIO()
        call_command('import_data', stdout=out)
        self.assertIn('Импорт данных успешно завершен', out.getvalue())