from django.db import models


class Position(models.Model):
    name = models.CharField('Название', max_length=100)


class Grade(models.Model):
    name = models.CharField('Название', max_length=100)


class Domen(models.Model):
    name = models.CharField('Название', max_length=100)


class TypeSkill(models.Model):
    name = models.CharField('Название', max_length=100)


class Competence(models.Model):
    name = models.CharField('Название', max_length=100)
    domen = models.ForeignKey(
        Domen, on_delete=models.CASCADE, verbose_name='домен'
    )
    type_skill = models.ForeignKey(
        TypeSkill, on_delete=models.CASCADE, verbose_name='Компетенция'
    )


class Skill(models.Model):
    name = models.CharField('Название', max_length=100)
    competence = models.ForeignKey(
        Competence, on_delete=models.CASCADE, verbose_name='Компетенция'
    )


class PositionRequirement(models.Model):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, verbose_name='Грейд'
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, verbose_name='Грейд'
    )
    rating = models.IntegerField('Оценка')
