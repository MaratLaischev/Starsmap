from django.contrib import admin

from specialties.models import (
    Position, Grade, Competence, Skill, PositionRequirement
)


class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class CompetenceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'domen',
        'type_skill'
    )


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'competence'
    )


class PositionRequirementAdmin(admin.ModelAdmin):
    list_display = (
        'position',
        'grade',
        'skill',
        'rating'
    )


admin.site.register(PositionRequirement, PositionRequirementAdmin)
admin.site.register(Competence, CompetenceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Position, PositionAdmin)
