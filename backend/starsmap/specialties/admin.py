from django.contrib import admin

from specialties.models import (
    Position, Grade, Competence, Skill, RequirementPosition
)


class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'grade',
    )


class CompetenceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type'
    )


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'competence'
    )


class RequirementPositionAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'grade',
        'skill',
        'rating'
    )


admin.site.register(RequirementPosition, RequirementPositionAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Position, PositionAdmin)
