from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from django.http import Http404
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class PostList(LoginRequiredMixin, generic.ListView):
    model = models.Note


class PostDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Note


class CreateNote(LoginRequiredMixin, generic.CreateView):
    model = models.Note
    form_class = forms.CreateNoteForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteNote(LoginRequiredMixin, generic.DeleteView):
    model = models.Note
    success_url = reverse_lazy('notes:list')

class UpdateNote(LoginRequiredMixin, generic.UpdateView):
    model = models.Note
    # fields = ('title', 'content')
    form_class = forms.CreateNoteForm
