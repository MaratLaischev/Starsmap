from django.db import models

from specialties.models import Grade, Position, Skill


class Team(models.Model):
    name = models.CharField('Название', max_length=100)


class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    bus_factor = models.BooleanField('Бас фактор')
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, verbose_name='Грейд'
    )


class TargetEmployee(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, verbose_name='Позиция'
    )
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, verbose_name='Грейд'
    )


class EmployeeTeam(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, verbose_name='Команда'
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name='Сотрудник'
    )


class RequestTraining(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name='Сотрудник'
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, verbose_name='Скилл'
    )
    desired_result = models.CharField('Желаемый результат', max_length=100)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    status = models.CharField('Статут запроса', max_length=100)


class Level(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name='Сотрудник'
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, verbose_name='Скилл'
    )
    data = models.DateField('Дата')
    evaluation = models.CharField('Оценка эксперта', max_length=100)
    name = models.CharField('Название', max_length=100) # Начинающий - Экспертный
    # accordance = models.CharField('Соответствие', max_length=100)
