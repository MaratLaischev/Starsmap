from pathlib import Path
import csv

from django.core.management.base import BaseCommand
from django.apps import apps
from django.db.utils import IntegrityError

from teams.models import (
    Team, Employee, Position, Grade, Target, EmployeeSkill, EmployeeCheck
)
from specialties.models import TypeSkill, Domen, Competence, Skill


class FileOpenException(Exception):
    """Вызов исключения при некорректном открытии файла."""

    pass


class Command(BaseCommand):
    """Команда для загрузки тестовых данных в базу данных"""

    help = "Загрузка данных для тестирования"

    def handle(self, *args, **kwargs):
            try:
                with open(f"static/bd.csv", newline='', encoding='utf-8') as f:
                    dataframe = csv.DictReader(f)
                    for row in dataframe:
                            team, _ = Team.objects.get_or_create(
                                name=row.get('team_name')
                            )
                            position, _ = Position.objects.get_or_create(
                                name=row.get('position_name')
                            )
                            grade, _ = Grade.objects.get_or_create(
                                name=row.get('grade_name')
                            )
                            employee, _ = Employee.objects.get_or_create(
                                team=team,
                                name_surname=row.get('employee_name_surname'),
                                position=position,
                                grade=grade,
                                bus_factor='TRUE'==row.get(
                                    'employee_bus_factor'
                                    ),
                                key='TRUE'==row.get(
                                    'employee_key'
                                    ),
                            )
                            Target.objects.get_or_create(
                                employee=employee,
                                grade=grade,
                                position=position
                            )
                            type_skill, _ = TypeSkill.objects.get_or_create(
                                name=row.get('type_skill_name')
                            )
                            domen, _ = Domen.objects.get_or_create(
                                name=row.get('domen_name')
                            )
                            competence, _= Competence.objects.get_or_create(
                                name=row.get('competence_name'),
                                domen=domen,
                                type_skill=type_skill
                            )
                            skill, _= Skill.objects.get_or_create(
                                name=row.get('skill_name'),
                                competence=competence
                            )
                            EmployeeSkill.objects.get_or_create(
                                employee=employee,
                                skill=skill,
                                key='TRUE'==row.get('employeeSkill_key'),
                                education_request='TRUE'==row.get(
                                    'employeeSkill_education_request'
                                )
                            )
                            EmployeeCheck.objects.get_or_create(
                                employee=employee,
                                skill=skill,
                                estimation=row.get('employeeCheck_estimation'),
                                accordance='TRUE'==row.get(
                                    'employeeCheck_accordance'
                                    ),
                                education_progress='TRUE'==row.get(
                                    'EmployeeCheck_education'
                                    ),
                            )
                
            except FileOpenException as error:
                self.stdout.write(f"Ошибка при открытии файла: {error}")
                
