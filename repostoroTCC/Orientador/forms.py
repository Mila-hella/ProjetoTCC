from django.forms import ModelForm
from .models import Orientador

class InsereOrientador(ModelForm):
    class Meta:
        model = Orientador
        fields = "__all__"