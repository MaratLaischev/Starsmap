from django.db import models

from teams.models import Employee, Position, Grade


class Competence(models.Model):
    """Модель компетенции."""
    name = models.CharField('Название', max_length=100)
    type = models.CharField('Тип', max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Модель навыков."""
    name = models.CharField('Название', max_length=100)
    competence = models.ForeignKey(
        Competence,
        on_delete=models.CASCADE,
        verbose_name='Компетенция'
    )

    def __str__(self):
        return self.name


class RequestTraining(models.Model):
    """Модель запроса на обучение."""
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name='Сотрудник'
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        verbose_name='Навык'
    )
    desired_result = models.CharField('Желаемый результат', max_length=100)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    status = models.CharField('Статус запроса', max_length=100)

    def __str__(self):
        return f'{self.employee.name_surname} - {self.skill.name}'


class Level(models.Model):
    """Модель уровня навыка сотрудника."""
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name='Сотрудник'
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        verbose_name='Навык'
    )
    data = models.DateField('Дата')
    evaluation = models.CharField('Оценка эксперта', max_length=100)
    name = models.CharField('Название', max_length=100)  # Например, Начинающий, Эксперт

    def __str__(self):
        return f'{self.employee.name_surname} - {self.skill.name}'


class RequirementPosition(models.Model):
    """Модель требований к позиции."""
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name='Позиция'
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        verbose_name='Грейд'
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        verbose_name='Навык'
    )
    rating = models.IntegerField('Оценка')

    def __str__(self):
        return f'{self.position.name} - {self.skill.name} - {self.rating}'
