import os

from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils.translation import ugettext as _

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib import auth
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import Project, Developer, Stage, Task


#-------------Project-----------------------------#
class ProjectDeveloperList(ListView):
    template_name = "web/developer_by_project.html"

    def get_queryset(self):
        self.project = get_object_or_404(Project, title=self.args[0])
        return Developer.objects.filter(project=self.project)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectDeveloperList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['project'] = self.project
        return context


class ProjectList(ListView):
    model = Project
    template_name = "web/projects.html"
    context_object_name = 'projects'
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        stages = []
        for project in self.queryset:
            project_stages = Stage.objects.filter(project__id=project.id)
            if project_stages:
                for stage in project_stages:
                    stages.append(stage)

        form = ManageProjectForm()
        context['form'] = form
        context['stages'] = stages
        return context


class ProjectDetail(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["stage"] = Stage.name
        return context


class CreateProject(CreateView):
    model = Project
    form_class = ManageProjectForm
    context_object_name = 'project'
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateProject, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateProject, self).get_context_data(**kwargs)
        context['form_url'] = self.object.get_create_url()
        return context

    def form_valid(self, form):
        super(CreateProject, self).form_valid(form)

        username = self.request.user.username
        email = self.request.user.email#"nllanes@gmail.com"
        print username
        print email

        filescrip = 'D:/Personal/Nueva carpeta/project_admin/apps/web/lib/DjangoBolt/django_bolt_script.py'
        archive = os.path.basename(filescrip)
        directorio = os.path.dirname(filescrip)
        print archive
        print directorio
        #os.startfile(filescrip , username)
        os.system(filescrip + ' ' + username + ' ' + email)
        return HttpResponseRedirect('/')

class UpdateProject(UpdateView):
    model = Project
    form_class = ManageProjectForm
    context_object_name = 'project'
    success_url = '/'
    template_name = 'web/manage_project.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateProject, self).get_context_data(**kwargs)
        context['form_url'] = self.object.get_update_url()
        return context


class DeleteProject(DeleteView):
    model = Project
    success_url = '/'


#------------------Task---------------------3
class TaskList(ListView):
    model = Task
    template_name = "web/task.html"
    context_object_name = 'tasks'
    queryset = Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        form = ManageStageForm()
        context['form'] = form
        return context


class CreateTask(CreateView):
    model = Task
    form_class = ManageTaskForm
    context_object_name = 'task'
    success_url = '/task'

    def get_context_data(self, **kwargs):
        context = super(CreateTask, self).get_context_data(**kwargs)
        context['form_url'] = self.object.get_create_url()
        return context


class UpdateTask(UpdateView):
    model = Task
    form_class = ManageTaskForm
    context_object_name = 'task'
    success_url = '/task'
    template_name = 'web/manage_task.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateTask, self).get_context_data(**kwargs)
        context['form_url'] = self.object.get_update_url()
        return context


class DeleteTask(DeleteView):
    model = Task
    success_url = '/task'


#-----------------Stage--------------------#
class StageList(ListView):
    model = Stage
    template_name = "web/stage.html"
    context_object_name = 'stages'
    queryset = Stage.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StageList, self).get_context_data(**kwargs)
        form = ManageStageForm()
        context['form'] = form
        return context


class CreateStage(CreateView):
    model = Stage
    form_class = ManageStageForm
    template_name = '/stage.html'
    context_object_name = 'stage'
    success_url = '/stage'

    def get_context_data(self, **kwargs):
        context = super(CreateStage, self).get_context_data(**kwargs)
        context['form_url'] = self.object.get_create_url()
        return context


class UpdateStage(UpdateView):
    model = Stage
    form_class = ManageStageForm
    context_object_name = 'stage'
    success_url = '/stage'
    template_name = 'web/manage_stage.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateStage, self).get_context_data(**kwargs)
        context['form_url'] = self.object.get_update_url()
        return context


class DeleteStage(DeleteView):
    model = Stage
    success_url = '/stage'

#----------Developer--------------------#


class DeveloperList(ListView):
    template_name = "web/new_developer.html"
    queryset = Developer.objects.order_by('-name')
    context_object_name = 'developer_list'


class Registration(CreateView):
    template_name = 'web/registration.html'
    form_class = UserRegisterForm
    success_url = '/'

    # def post(self, request, *args, **kwargs):
    #    reg_form = ClientRegisterForm(request.POST)
    #    if reg_form.is_valid():
    #        reg_form.save()
    #        return HttpResponseRedirect(self.success_url)
    #    else:
    #        return render_to_response('reserve/registration.html', {'form': reg_form},
    # context_instance=RequestContext(request))


############################Para autenticarse#############################
#def login(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = auth.authenticate(username=username, password=password)
#    if user is not None and user.is_active:
#        auth.login(request, user)
#        return HttpResponseRedirect("/project")
#    else:
#        return HttpResponseRedirect("/registration")


#def logout(request):
#    auth.logout(request)
#    # Redirect to a success page.
#    return HttpResponseRedirect("/loggedout")
