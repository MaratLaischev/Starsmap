from io import StringIO

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class GradeDataViewSetTest(TestCase):
    # Настройка клиента и URL для тестов
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("grades-list")

    # Тест на получение списка уровней
    def test_list_grades(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SkillViewSetTest(TestCase):
    # Настройка клиента и URL для тестов
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("skill-list")

    # Тест на получение списка навыков
    def test_list_skills(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PositionViewSetTest(TestCase):
    # Настройка клиента и URL для тестов
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("positions-list")

    # Тест на получение списка должностей
    def test_list_positions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CompetenceViewSetTest(TestCase):
    # Настройка клиента и URL для тестов
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("competences-list")

    # Тест на получение списка компетенций
    def test_list_competences(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RequirementPositionViewSetTest(TestCase):
    # Настройка клиента и URL для тестов
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("requirementpositions-list")

    # Тест на получение списка требований к должностям
    def test_list_requirement_positions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamViewSetTest(TestCase):
    # Настройка клиента и URL для тестов
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("team-list")
        self.team_data = {"name": "Test Team"}

    # Тест на создание команды
    def test_create_team(self):
        response = self.client.post(self.url, self.team_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Тест на получение списка команд
    def test_list_teams(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SpecialityDataViewSetTest(TestCase):
    # Настройка клиента и URL для тестов
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("specialities-list")

    # Тест на получение списка специальностей
    def test_list_specialities(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ImportDataCommandTest(TestCase):
    # Тест на импорт данных
    def test_import_data(self):
        out = StringIO()
        call_command("import_data", stdout=out)
        self.assertIn("Импорт данных успешно завершен", out.getvalue())
