from django.db import models

# from teams.models import Employee


class Position(models.Model):
    name = models.CharField('Название', max_length=100)


class Grade(models.Model):
    grade = models.CharField(max_length=100)


class Competence(models.Model):
    name = models.CharField('Название', max_length=100)
    type = models.CharField('Тип', max_length=100)


class Skill(models.Model):
    name = models.CharField('Название', max_length=100)
    competence = models.ForeignKey(
        Competence, on_delete=models.CASCADE, verbose_name='Компетенция'
    )


class RequirementPosition(models.Model):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, verbose_name='Гейд'
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, verbose_name='Гейд'
    )
    rating = models.IntegerField('Оценка')
