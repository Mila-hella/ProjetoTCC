from django.forms import ModelForm
from .models import Curso

class InsereCurso(ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"