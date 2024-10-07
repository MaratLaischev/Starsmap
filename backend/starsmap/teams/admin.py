from django.contrib import admin

from teams.models import (
    Team, Employee, TargetEmployee, EmployeeTeam, RequestTraining, Level
)


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'bus_factor',
        'position',
        'grade'
    )


class TargetEmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'position',
        'grade'
    )


class EmployeeTeamAdmin(admin.ModelAdmin):
    list_display = (
        'team',
        'employee'
    )


class RequestTrainingAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'skill',
        'desired_result',
        'start_date',
        'end_date',
        'status'
    )


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'skill',
        'data',
        'evaluation',
        'name'
    )


admin.site.register(Team, TeamAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TargetEmployee, TargetEmployeeAdmin)
admin.site.register(EmployeeTeam, EmployeeTeamAdmin)
admin.site.register(RequestTraining, RequestTrainingAdmin)
admin.site.register(Level, LevelAdmin)
