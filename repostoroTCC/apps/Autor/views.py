from .models import Autor
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import InsereAutor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    template_name: str = "autor/home.html"

@login_required
def AutorUploadView(request):
    if request.method == 'POST':
        form = InsereAutor(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy("listAutor"))
    else:
        form = InsereAutor()
    return render(request, 'forms/register.html', {"form":form, "title":"Autor"})

#Parte de Acesso e Edit de User
class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    fields = "__all__"
    template_name = "autor/detail.html"
    success_url = "/"

#Deletar Usuário
class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = "/autor/"
    template_name = "autor/delete.html"
