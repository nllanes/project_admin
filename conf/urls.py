from django.conf.urls import patterns, include, url
from django_countries import settings
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()

from apps.web import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ProjectList.as_view()),
    url(r'^resources/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}, name='resource'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^task/$', views.TaskList.as_view()),
    url(r'^stage/$', views.StageList.as_view()),
    url(r'^developer/([\w-]+)/$', views.ProjectDeveloperList.as_view()),
    url(r'^new_developer/$', views.DeveloperList.as_view()),

    url(r'^create_project/', views.CreateProject.as_view(), name='create_project'),
    url(r'^create_stage/', views.CreateStage.as_view(), name='create_stage'),
    url(r'^create_task/', views.CreateTask.as_view(), name='create_task'),

    url(r'^update_project/(?P<pk>[^\.]+)$',
        views.UpdateProject.as_view(), name='update_project'),
    url(r'^update_task/(?P<pk>[^\.]+)$',
        views.UpdateTask.as_view(), name='update_task'),
    url(r'^update_stage/(?P<pk>[^\.]+)$',
        views.UpdateStage.as_view(), name='update_stage'),

    url(r'^delete_project/(?P<pk>[^\.]+)$',
        views.DeleteProject.as_view(), name='delete_project'),
    url(r'^delete_task/(?P<pk>[^\.]+)$',
        views.DeleteTask.as_view(), name='delete_task'),
    url(r'^delete_stage/(?P<pk>[^\.]+)$',
        views.DeleteStage.as_view(), name='delete_stage'),

    url(r'^login/$', login, {'template_name': 'web/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGIN_REDIRECT_URL},
        name='logout'),

)
