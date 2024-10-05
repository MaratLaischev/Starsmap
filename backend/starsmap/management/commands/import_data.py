import csv
from django.core.management.base import BaseCommand
from teams.models import Employee, Team, Grade, Skill, Position
from specialties.models import Competence, Position, Skill, #Domen
from datetime import datetime


class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        with open(options['csv_file'], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                team, _ = Team.objects.get_or_create(name=row['команда'])
                grade, _ = Grade.objects.get_or_create(name=row['грейд'])
                position, _ = Position.objects.get_or_create(name=row['должность'])
                competency, _ = Competence.objects.get_or_create(name=row['компетенция'])
                #domen, _ = Domen.objects.get_or_create(name=row['домен']) нужна модель
                skill, _ = Skill.objects.get_or_create(name=row['навык'], competency=competency)

                employee, created = Employee.objects.update_or_create(
                    id=row['id'],
                    defaults={
                        'name': row['сотрудник'].split()[0],
                        'surname': row['сотрудник'].split()[1],
                        'position': position,
                        'grade': grade,
                        'bas_factor': row['bf'] == 'yes',
                        'education_request': int(row['education']) if row['education'] else None,
                    }
                )

                team.employees.add(employee)

                Skill.objects.update_or_create(
                    employee=employee,
                    skill=skill,
                    defaults={
                        'level': row['оценка_char'],
                        'date_check': datetime.strptime(row['дата'], '%Y-%m-%d'),
                        'estimation': int(row['оценка_int']),
                        'conformance': row['соответствие'],
                        'next_check': datetime.strptime(row['next_check'], '%Y-%m-%d'),
                        'get_checked': row['get_checked'] == 'True',
                    }
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
# Для запуска python manage.py import_data path/to/your/bd.csv
