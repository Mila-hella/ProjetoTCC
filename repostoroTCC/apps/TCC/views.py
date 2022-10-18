from .models import TCC
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import InsereTCC
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class TCCListView(ListView):
    model = TCC
    template_name: str = "tcc/home.html"

@login_required
def TCCUploadView(request):
    if request.method == 'POST':
        form = InsereTCC(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy("listTCC"))
    else:
        form = InsereTCC()
    return render(request, 'forms/register.html', {"form":form, "title":"TCC"})

#Parte de Acesso e Edit de User
class TCCUpdateView(LoginRequiredMixin, UpdateView):
    model = TCC
    fields = "__all__"
    template_name = "tcc/detail.html"
    success_url = "/"

#Deletar Usuário
class TCCDeleteView(LoginRequiredMixin, DeleteView):
    model = TCC
    success_url = "/"
    template_name = "tcc/delete.html"
