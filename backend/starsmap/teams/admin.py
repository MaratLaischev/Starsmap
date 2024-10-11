from django.contrib import admin

from teams.models import (
    Team, Employee, Target, EmployeeSkill
)


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name_surname',
        'bus_factor',
        'position',
        'grade'
    )


class TargetAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'position',
        'grade'
    )

class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'skill',
        'key',
        'education_request'
    )


admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Target, TargetAdmin)
admin.site.register(EmployeeSkill, EmployeeSkillAdmin)
