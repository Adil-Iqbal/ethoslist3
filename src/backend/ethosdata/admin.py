from django.contrib import admin
from models import Clip, Episode, Project

class ClipAdmin(admin.ModelAdmin):
    list_display = (id)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = (id)


class ProjectAdmin(admin.ModelAdmin):
    list_display = (id)


# Register your models here.
admin.site.register(Clip, ClipAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Project, ProjectAdmin)
