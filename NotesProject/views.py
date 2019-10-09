from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404


from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from braces.views import SelectRelatedMixin
from django.views import generic

from . import forms
from storageApp import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

##########

class NoteList(SelectRelatedMixin, generic.ListView):
    model = models.Note
    select_related = ("user",)


class UserNotes(generic.ListView):
    model = models.Note
    template_name = "storageApp/user_note_list.html"

    def get_queryset(self):
        try:
            self.note_user = User.objects.prefetch_related("notes").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.note_user.notes.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["note_user"] = self.note_user
        return context


class NoteDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Note
    select_related = ("user", "note")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreateNote(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('title', 'message',)
    model = models.Note

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteNote(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Note
    select_related = ("user",)
    success_url = reverse_lazy("notes:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Note Deleted")
        return super().delete(*args, **kwargs)
