from django.forms import ModelForm
from . import models


class AddTaskForm(ModelForm):
    class Meta:
        model = models.Task
        fields = [
            'title',
            'content',
            'completed'
        ]


class UpdateTaskForm(ModelForm):
    class Meta:
        model = models.Task
        fields = [
            'title',
            'content',
            'completed'
        ]


class DeleteTaskForm(ModelForm):
    class Meta:
        model = models.Task
        fields = [
            'title',
            'content',
            'completed'
        ]
