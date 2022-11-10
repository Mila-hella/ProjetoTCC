from django.forms import ModelForm
from .models import Autor

class InsereAutor(ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"