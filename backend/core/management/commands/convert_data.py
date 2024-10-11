import pandas as pd
import json
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Импорт данных из файла employees.xlsx и конвертация в формат JSON'

    def handle(self, *args, **kwargs):

        df = pd.read_excel('employees.xlsx')

        def transform_data(group):
            employee_info = group.iloc[0]
            return {
                "employee_id": int(employee_info["employee_id"]),
                "employee_name_surname": employee_info["employee_name_surname"],
                "employee_position_name": employee_info["employee_position_name"],
                "employee_team_name": employee_info["employee_team_name"],
                "employee_grade_name": employee_info["employee_grade_name"],
                "employee_bus_factor": bool(employee_info["employee_bus_factor"]),
                "employee_key": bool(employee_info["employee_key"]),
                "skills": [
                    {
                        "skill_name": row["skill_name"],
                        "skill_competence_name": row["skill_competence_name"],
                        "skill_domain_name": row["skill_domain_name"],
                        "skill_hard_soft_type": row["skill_hard_soft_type"],
                        "skill_estimation": int(row["skill_estimation"]),
                        "skill_accordance": bool(row["skill_accordance"]),
                        "skill_key": bool(row["skill_key"]),
                        "skill_education_request": bool(row["skill_education_request"]),
                        "skill_education_in_progress": bool(row["skill_education_in_progress"]),
                    }
                    for _, row in group.iterrows()
                ]
            }

        grouped = df.groupby('employee_id')

        employees = [transform_data(group) for _, group in grouped]

        with open('employees.json', 'w', encoding='utf-8') as f:
            json.dump(employees, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS('Данные успешно сконвертированы и сохранены в файл employees.json'))