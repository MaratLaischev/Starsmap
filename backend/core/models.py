from django.db import models


class Competence(models.Model):
    """Модель компетенции."""
    name = models.CharField('Название', max_length=100)
    type = models.CharField('Тип', max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Модель навыков."""
    name = models.CharField('Название', max_length=100)
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, verbose_name='Компетенция')
    domain_name = models.CharField('Домен', max_length=100)
    hard_soft_type = models.CharField('Тип', max_length=10)
    estimation = models.IntegerField('Оценка')
    accordance = models.BooleanField('Соответствие')
    key = models.BooleanField('Ключевой')
    education_request = models.BooleanField('Запрос на обучение')
    education_in_progress = models.BooleanField('Обучение в процессе')

    def __str__(self):
        return self.name


class Position(models.Model):
    """Модель позиции."""
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    """Модель грейда."""
    grade = models.CharField('Грейд', max_length=100)

    def __str__(self):
        return self.grade


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
    bus_factor = models.BooleanField(default=False)
    key = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name_surname


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
        return f"{self.employee} - {self.skill}"


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
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return f"{self.employee} - {self.skill} - {self.name}"


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
        return f"{self.position} - {self.grade} - {self.skill}"