from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["mainTitle", "mainContent"]
        widgets = {"mainTitle": TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Name'}),
                   "mainContent": Textarea(attrs={'class': 'form-control',
                                                  'placeholder': 'Name'})
                   }