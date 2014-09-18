from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView

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


class TaskList(ListView):
    model = Task
    template_name = "web/task.html"
    context_object_name = 'tasks'
    queryset = Task.objects.all()


class ProjectDetail(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["stage"] = Stage.name
        return context


class DeveloperList(ListView):
    template_name = "web/new_developer.html"
    queryset = Developer.objects.order_by('-name')
    context_object_name = 'developer_list'


class CreateProject(CreateView):
    template_name = 'web/create_project.html'
    form_class = CreateProjectForm
    context_object_name = 'create_project'
    success_url = 'web/projects.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateProject, self).dispatch(*args, **kwargs)

   # def form_valid(self, form):
   #     current_user = self.request.user

        #Loading the information of the client related to the current logged user
   #     try:
   #         client_user = Developer.objects.get(user__username=current_user.username)
   #     except Developer.DoesNotExist:
   #         client_user = None


class CreateStage(CreateView):
    template_name = 'web/create_stage.html'
    form_class =  CreateStageForm
    context_object_name = 'create_stage'


class CreateTask(CreateView):
    template_name = 'web/create_task.html'
    form_class = CreateTaskForm
    context_object_name = 'create_task'


class Registration(CreateView):
    template_name = 'web/registration.html'
    form_class = UserRegisterForm
    success_url = '/'

    #def post(self, request, *args, **kwargs):
    #    reg_form = ClientRegisterForm(request.POST)
    #    if reg_form.is_valid():
    #        reg_form.save()
    #        return HttpResponseRedirect(self.success_url)
    #    else:
    #        return render_to_response('reserve/registration.html', {'form': reg_form},
    #                                  context_instance=RequestContext(request))


############################Para autenticarse####################################
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.

        return render_to_response('web/projects.html')
    else:
        # Show an error page
        return HttpResponseRedirect("/registration")


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/loggedout")

