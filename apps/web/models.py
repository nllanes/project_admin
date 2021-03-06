from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.core.urlresolvers import reverse

from tinymce.models import HTMLField

LEVEL_CHOICES = (
    ('becario', _(u'Becario')),
    ('junior', _(u'Junior')),
    ('senior', _(u'Senior'))
)

STATUS_CHOICES = (
    ('inicio', _(u'Inicio')),
    ('development', _(u'Development')),
    ('design', _(u'Design')),
    ('finished', _(u'Finished'))
)

PRIORITY_CHOICES = (
    ('normal', _(u'Normal')),
    ('media', _(u'Media')),
    ('urgent', _(u'Urgent'))
)

SPECIALTY_CHOICE = (
    ('informatic', _(u'Informatic')),
    ('designer', _(u'Designer')),
    ('cyber', _(u'Cyber'))
)


class Developer(models.Model):
    """
    Model to represent a Developer
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('Usuario'))
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    specialty = models.CharField(max_length=50, choices=SPECIALTY_CHOICE)
    developer_picture = models.ImageField(blank=True, upload_to='developers')

    def __unicode__(self):
        return self.user.username


class Project(models.Model):
    """
    Model to represent a Project
    """
    title = models.CharField(max_length=50)
    description = HTMLField(verbose_name=_('Description'), blank=True, default='')

    class Meta:
        ordering = ["-title"]

    def __unicode__(self):
        return self.title

    def get_create_url(self):
        return reverse('web.views.CreateProject', args=[str(self.id)])

    def get_update_url(self):
        return reverse('update_project', kwargs={'pk': str(self.id)})


class Stage(models.Model):
    """
     Model to represent a Stage
    """
    name = models.CharField(max_length=50)
    init_date = models.DateTimeField('Inicio')
    end_date = models.DateTimeField('End')
    project = models.ForeignKey(Project, related_name='project_stage')

    class Meta:
        ordering = ["-init_date"]

    def __unicode__(self):
        return self.name

    def get_create_url(self):
        return reverse('web.views.CreateStage', args=[str(self.id)])

    def get_update_url(self):
        return reverse('update_stage', kwargs={'pk': str(self.id)})


class Task(models.Model):
    """
    Model to represent a Task
    """
    name = models.CharField(max_length=10)
    description = HTMLField(verbose_name=_('Description'),
                            blank=True, default='')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(Project)
    assigned_to_developer = models.ForeignKey(Developer)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        ordering = ["-priority"]

    def __unicode__(self):
        return self.name

    def get_create_url(self):
        return reverse('web.views.CreateTask', args=[str(self.id)])

    def get_update_url(self):
        return reverse('update_task', kwargs={'pk': str(self.id)})
