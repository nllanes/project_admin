from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django_countries import settings
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

from apps.web.views import *


urlpatterns = patterns(
    '',
    url(r'^$', ProjectList.as_view()),

    # Examples:
    # url(r'^$', 'project_admin.views.home', name='home'),
    # url(r'^project_admin/', include('project_admin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^projects/$', ProjectList.as_view()),
    url(r'^task/$', TaskList.as_view()),
    url(r'^developer/([\w-]+)/$', ProjectDeveloperList.as_view()),
    url(r'^new_developer/$', DeveloperList.as_view()),
    #url(r'^registration/', Registration.as_view(), name='registration'),
    url(r'^create_project/', CreateProject.as_view(), name='create_project'),
    url(r'^update_project/$', UpdateProject.as_view(), name='update_project'),
    url(r'^create_stage/', CreateStage.as_view(), name='create_stage'),
    url(r'^create_task/', CreateTask.as_view(), name='create_task'),
    url(r'^login/', login, {'template_name': 'web/login.html'}, name='login'),
    url(r'^logout/', logout, {'next_page': settings.LOGIN_REDIRECT_URL},
        name='logout'),

)
