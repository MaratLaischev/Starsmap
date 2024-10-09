from django.db import models


class Team(models.Model):
    """Модель команды."""
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Модель сотрудника."""
    name_surname = models.CharField('Имя', max_length=100)
    position = models.CharField('Позиция', max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=50)
    hard_skills = models.JSONField()
    soft_skills = models.JSONField()
    bf = models.BooleanField(default=False)
    key = models.BooleanField(default=False)
    education_request = models.BooleanField(default=False)
    education_in_progress = models.BooleanField(default=False)

    def __str__(self):
        return self.name_surname


class Position(models.Model):
    """Модель позиции сотрудника."""
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    """Модель грейда сотрудника."""
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.grade
