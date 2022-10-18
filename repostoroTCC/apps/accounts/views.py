from multiprocessing import context
from django.contrib.auth.views import PasswordChangeView
from .forms import CadastroForm 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin

class UserCreateView(CreateView):
    form_class = CadastroForm
    template_name = 'forms/register.html'
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context["title"] = "Cadastro User"
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["username", "email", "first_name", "last_name"]
    template_name = "profile.html"
    success_url = "/"

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = "/"
    template_name = "delete.html"

class PasswordView(LoginRequiredMixin, PasswordChangeView):
    model = User
    success_url = "/"
    template_name = "forms/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["botao"] = "Nova Senha"
        context["title"] = "Modificar Senha"
        context["descricao"] = "Modificar Senha"

        return context