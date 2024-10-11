from django.db import models

from specialties.models import Grade, Position, Skill


class Team(models.Model):
    name = models.CharField('Название', max_length=100)


class Employee(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, verbose_name='Команда'
    )
    name_surname = models.CharField('Имя', max_length=100)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, verbose_name='Грейд'
    )
    bus_factor = models.BooleanField('Бас фактор')
    key = models.BooleanField('Ключевой сотрудник')

    class Meta:
        default_related_name = 'employee'


class Target(models.Model):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, verbose_name='Грейд'
    )


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, verbose_name='Скил'
    )
    key = models.BooleanField('Ключевой навык')
    education_request = models.BooleanField('Образовательный запрос')

    class Meta:
        default_related_name = 'employee_skill'

class EmployeeCheck(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, verbose_name='Скил'
    )
    estimation = models.IntegerField('Оценка')
    accordance = models.BooleanField('Соответствие')
    education_progress = models.BooleanField('Обучается')
    
    class Meta:
        default_related_name = 'employee_check'
