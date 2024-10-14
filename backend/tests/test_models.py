from django.test import TestCase
from core.models import (
    Competence, Skill, Employee, Team, Position, Grade, RequestTraining, Level, RequirementPosition
)


class CompetenceModelTest(TestCase):
    def test_create_competence(self):
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        self.assertEqual(competence.name, "Test Competence")
        self.assertEqual(competence.type, "Soft")

    def test_update_competence(self):
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        competence.name = "Updated Competence"
        competence.save()
        self.assertEqual(competence.name, "Updated Competence")

    def test_delete_competence(self):
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        competence_id = competence.id
        competence.delete()
        self.assertFalse(Competence.objects.filter(id=competence_id).exists())


class SkillModelTest(TestCase):
    def test_create_skill(self):
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        self.assertEqual(skill.name, "Test Skill")
        self.assertEqual(skill.competence, competence)

    def test_update_skill(self):
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        skill.name = "Updated Skill"
        skill.save()
        self.assertEqual(skill.name, "Updated Skill")

    def test_delete_skill(self):
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        skill_id = skill.id
        skill.delete()
        self.assertFalse(Skill.objects.filter(id=skill_id).exists())


class PositionModelTest(TestCase):
    def test_create_position(self):
        position = Position.objects.create(name="Test Position")
        self.assertEqual(position.name, "Test Position")

    def test_update_position(self):
        position = Position.objects.create(name="Test Position")
        position.name = "Updated Position"
        position.save()
        self.assertEqual(position.name, "Updated Position")

    def test_delete_position(self):
        position = Position.objects.create(name="Test Position")
        position_id = position.id
        position.delete()
        self.assertFalse(Position.objects.filter(id=position_id).exists())


class GradeModelTest(TestCase):
    def test_create_grade(self):
        grade = Grade.objects.create(grade="Junior")
        self.assertEqual(grade.grade, "Junior")

    def test_update_grade(self):
        grade = Grade.objects.create(grade="Junior")
        grade.grade = "Senior"
        grade.save()
        self.assertEqual(grade.grade, "Senior")

    def test_delete_grade(self):
        grade = Grade.objects.create(grade="Junior")
        grade_id = grade.id
        grade.delete()
        self.assertFalse(Grade.objects.filter(id=grade_id).exists())

class RequirementPositionModelTest(TestCase):
    def test_create_requirement_position(self):
        position = Position.objects.create(name="Test Position")
        grade = Grade.objects.create(grade="Junior")
        skill = Skill.objects.create(name="Test Skill", competence=Competence.objects.create(name="Test Competence", type="Soft"), domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        requirement_position = RequirementPosition.objects.create(position=position, grade=grade, skill=skill, rating=5)
        self.assertEqual(requirement_position.rating, 5)

    def test_update_requirement_position(self):
        position = Position.objects.create(name="Test Position")
        grade = Grade.objects.create(grade="Junior")
        skill = Skill.objects.create(name="Test Skill", competence=Competence.objects.create(name="Test Competence", type="Soft"), domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        requirement_position = RequirementPosition.objects.create(position=position, grade=grade, skill=skill, rating=5)
        requirement_position.rating = 10
        requirement_position.save()
        self.assertEqual(requirement_position.rating, 10)

    def test_delete_requirement_position(self):
        position = Position.objects.create(name="Test Position")
        grade = Grade.objects.create(grade="Junior")
        skill = Skill.objects.create(name="Test Skill", competence=Competence.objects.create(name="Test Competence", type="Soft"), domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        requirement_position = RequirementPosition.objects.create(position=position, grade=grade, skill=skill, rating=5)
        requirement_position_id = requirement_position.id
        requirement_position.delete()
        self.assertFalse(RequirementPosition.objects.filter(id=requirement_position_id).exists())

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

    def test_update_team(self):
        team = Team.objects.create(name="Test Team")
        team.name = "Updated Team"
        team.save()
        self.assertEqual(team.name, "Updated Team")

    def test_delete_team(self):
        team = Team.objects.create(name="Test Team")
        team_id = team.id
        team.delete()
        self.assertFalse(Team.objects.filter(id=team_id).exists())

class EmployeeModelTest(TestCase):
    def test_create_employee(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        self.assertEqual(employee.name_surname, "Test User")

    def test_update_employee(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        employee.name_surname = "Updated User"
        employee.save()
        self.assertEqual(employee.name_surname, "Updated User")

    def test_delete_employee(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        employee_id = employee.id
        employee.delete()
        self.assertFalse(Employee.objects.filter(id=employee_id).exists())

class RequestTrainingModelTest(TestCase):
    def test_create_request_training(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        request_training = RequestTraining.objects.create(employee=employee, skill=skill, desired_result="Improve Skill", start_date="2023-01-01", end_date="2023-12-31", status="Pending")
        self.assertEqual(request_training.desired_result, "Improve Skill")

    def test_update_request_training(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        request_training = RequestTraining.objects.create(employee=employee, skill=skill, desired_result="Improve Skill", start_date="2023-01-01", end_date="2023-12-31", status="Pending")
        request_training.desired_result = "Master Skill"
        request_training.save()
        self.assertEqual(request_training.desired_result, "Master Skill")

    def test_delete_request_training(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        request_training = RequestTraining.objects.create(employee=employee, skill=skill, desired_result="Improve Skill", start_date="2023-01-01", end_date="2023-12-31", status="Pending")
        request_training_id = request_training.id
        request_training.delete()
        self.assertFalse(RequestTraining.objects.filter(id=request_training_id).exists())

class LevelModelTest(TestCase):
    def test_create_level(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        level = Level.objects.create(employee=employee, skill=skill, data="2023-01-01", evaluation="Expert", name="Level 1")
        self.assertEqual(level.evaluation, "Expert")

    def test_update_level(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        level = Level.objects.create(employee=employee, skill=skill, data="2023-01-01", evaluation="Expert", name="Level 1")
        level.evaluation = "Master"
        level.save()
        self.assertEqual(level.evaluation, "Master")

    def test_delete_level(self):
        team = Team.objects.create(name="Test Team")
        employee = Employee.objects.create(name_surname="Test User", position="Developer", team=team, grade="Junior", bus_factor=True, key=True)
        competence = Competence.objects.create(name="Test Competence", type="Soft")
        skill = Skill.objects.create(name="Test Skill", competence=competence, domain_name="Test Domain", hard_soft_type="Hard", estimation=5, accordance=True, key=True, education_request=False, education_in_progress=False)
        level = Level.objects.create(employee=employee, skill=skill, data="2023-01-01", evaluation="Expert", name="Level 1")
        level_id = level.id
        level.delete()
        self.assertFalse(Level.objects.filter(id=level_id).exists())