from .models import Orientador
from django.views.generic.list import ListView
from django.views.generic import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import InsereOrientador

class OrientadorListView(LoginRequiredMixin, ListView):
    model = Orientador
    template_name: str = "orientador/home.html"

class OrientadorCreateView(LoginRequiredMixin, CreateView):
    model = Orientador
    form_class = InsereOrientador
    success_url = "/orientador/"
    template_name = "forms/register.html"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Curso"
        return data
    
class OrientadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Orientador
    fields = "__all__"
    template_name = "orientador/detail.html"
    success_url = "/orientador/"

class OrientadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Orientador
    success_url = "/orientador/"
    template_name = "orientador/delete.html"