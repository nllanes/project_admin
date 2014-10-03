from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.web.models import Developer, Project, Stage, Task


class ManageProjectForm(forms.ModelForm):
    class Meta:
        model = Project


class ManageStageForm(forms.ModelForm):
    class Meta:
        model = Stage


class ManageTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        widgets = {
            'init_date': widgets.AdminSplitDateTime(),
            'end_date': widgets.AdminSplitDateTime()
        }


class UserRegisterForm(UserCreationForm):
    developer_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'developer_picture')

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=True)
        developer_user = Developer(user=user, developer_picture=self.cleaned_data['developer_picture'])

        if commit:
            developer_user.save()

        return developer_user
