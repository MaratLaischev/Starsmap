from django.contrib import admin
from core.models import (
    Position, Grade, Competence, Skill, RequirementPosition, Team,
    Employee, RequestTraining, Level
)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade',)


class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'competence')


class RequirementPositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'grade', 'skill', 'rating')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'position', 'team', 'grade', 'bus_factor', 'key')


class RequestTrainingAdmin(admin.ModelAdmin):
    list_display = (
        'employee', 'skill', 'desired_result', 'start_date', 'end_date', 'status',
    )


class LevelAdmin(admin.ModelAdmin):
    list_display = ('employee', 'skill', 'data', 'evaluation', 'name')


admin.site.register(Position, PositionAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(RequirementPosition, RequirementPositionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(RequestTraining, RequestTrainingAdmin)
admin.site.register(Level, LevelAdmin)
