from django import forms
from . import models

class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title','content']
        # widgets = {
        #     'content': forms.Textarea(attrs={'class':'editable'})
        # }
