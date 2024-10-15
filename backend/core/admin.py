from django.contrib import admin

from core.models import (
    Competence,
    Employee,
    Grade,
    Level,
    Position,
    RequestTraining,
    RequirementPosition,
    Skill,
    Team,
)


class PositionAdmin(admin.ModelAdmin):
    """Админ-панель для модели Position."""

    list_display = ("name",)


class GradeAdmin(admin.ModelAdmin):
    """Админ-панель для модели Grade."""

    list_display = ("grade",)


class CompetenceAdmin(admin.ModelAdmin):
    """Админ-панель для модели Competence."""

    list_display = ("name", "type")


class SkillAdmin(admin.ModelAdmin):
    """Админ-панель для модели Skill."""

    list_display = ("name", "competence")


class RequirementPositionAdmin(admin.ModelAdmin):
    """Админ-панель для модели RequirementPosition."""

    list_display = ("position", "grade", "skill", "rating")


class TeamAdmin(admin.ModelAdmin):
    """Админ-панель для модели Team."""

    list_display = ("name",)


class EmployeeAdmin(admin.ModelAdmin):
    """Админ-панель для модели Employee."""

    list_display = ("name_surname", "position", "team", "grade", "bus_factor", "key")


class RequestTrainingAdmin(admin.ModelAdmin):
    """Админ-панель для модели RequestTraining."""

    list_display = (
        "employee",
        "skill",
        "desired_result",
        "start_date",
        "end_date",
        "status",
    )


class LevelAdmin(admin.ModelAdmin):
    """Админ-панель для модели Level."""

    list_display = ("employee", "skill", "data", "evaluation", "name")


admin.site.register(Position, PositionAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(RequirementPosition, RequirementPositionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(RequestTraining, RequestTrainingAdmin)
admin.site.register(Level, LevelAdmin)
