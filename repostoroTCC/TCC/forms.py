from django.forms import ModelForm
from .models import TCC

class InsereTCC(ModelForm):
    class Meta:
        model = TCC
        fields = "__all__"