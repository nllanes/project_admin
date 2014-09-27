from django.conf.urls import patterns, include, url
from django_countries import settings
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

from apps.web.views import *


urlpatterns = patterns(
    '',
    url(r'^$', ProjectList.as_view()),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^task/$', TaskList.as_view()),
    url(r'^stage/$', StageList.as_view()),
    url(r'^developer/([\w-]+)/$', ProjectDeveloperList.as_view()),
    url(r'^new_developer/$', DeveloperList.as_view()),

    url(r'^create_project/', CreateProject.as_view(), name='create_project'),
    url(r'^create_stage/', CreateStage.as_view(), name='create_stage'),
    url(r'^create_task/', CreateTask.as_view(), name='create_task'),

    url(r'^update_project/(?P<pk>[^\.]+)$',
        UpdateProject.as_view(), name='update_project'),
    url(r'^update_task/(?P<pk>[^\.]+)$',
        UpdateTask.as_view(), name='update_task'),
    url(r'^update_stage/(?P<pk>[^\.]+)$',
        UpdateStage.as_view(), name='update_stage'),

    url(r'^delete_project/(?P<pk>[^\.]+)$',
        DeleteProject.as_view(), name='delete_project'),
    url(r'^delete_task/(?P<pk>[^\.]+)$',
        DeleteTask.as_view(), name='delete_task'),
    url(r'^delete_stage/(?P<pk>[^\.]+)$',
        DeleteStage.as_view(), name='delete_stage'),

    url(r'^login/', login, {'template_name': 'web/login.html'}, name='login'),
    url(r'^logout/', logout, {'next_page': settings.LOGIN_REDIRECT_URL},
        name='logout'),

)
