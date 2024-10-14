import json
from django.core.management.base import BaseCommand
from core.models import Employee, Skill, Competence


class Command(BaseCommand):
    help = 'Импорт данных из файла employees.json в базу данных'

    def handle(self, *args, **kwargs):
        with open('employees.json', 'r', encoding='utf-8') as f:
            employees = json.load(f)

        for employee_data in employees:
            employee, created = Employee.objects.get_or_create(
                id=employee_data["employee_id"],
                defaults={
                    "name_surname": employee_data["employee_name_surname"],
                    "position": employee_data["employee_position_name"],
                    "team": employee_data["employee_team_name"],
                    "grade": employee_data["employee_grade_name"],
                    "bus_factor": employee_data["employee_bus_factor"],
                    "key": employee_data["employee_key"],
                },
            )

            for skill_data in employee_data["skills"]:
                competence, _ = Competence.objects.get_or_create(
                    name=skill_data["skill_competence_name"]
                )
                Skill.objects.get_or_create(
                    name=skill_data["skill_name"],
                    competence=competence,
                    defaults={
                        "domain_name": skill_data["skill_domain_name"],
                        "hard_soft_type": skill_data["skill_hard_soft_type"],
                        "estimation": skill_data["skill_estimation"],
                        "accordance": skill_data["skill_accordance"],
                        "key": skill_data["skill_key"],
                        "education_request": skill_data["skill_education_request"],
                        "education_in_progress": skill_data[
                            "skill_education_in_progress"
                        ],
                    },
                )
