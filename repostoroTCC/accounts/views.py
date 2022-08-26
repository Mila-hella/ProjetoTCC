from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'register.html', {'form':form})

#Parte de Acesso e Edit de User
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["username", "email", "first_name", "last_name"]
    template_name = "profile.html"
    success_url = "/"

#Deletar Usuário
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = "/"
    template_name = "delete.html"

