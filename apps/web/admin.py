__author__ = 'nllanes'


from django.contrib import admin
from apps.web.models import Developer, Project, Stage, Task

admin.site.register(Developer)
admin.site.register(Stage)
admin.site.register(Project)
admin.site.register(Task)