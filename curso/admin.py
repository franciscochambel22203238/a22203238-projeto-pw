from django.contrib import admin
from .models import Course, ScientificArea, Discipline, ProgrammingLanguage, Project, Teacher

admin.site.register(Course)
admin.site.register(ScientificArea)
admin.site.register(Discipline)
admin.site.register(ProgrammingLanguage)
admin.site.register(Teacher)
admin.site.register(Project)