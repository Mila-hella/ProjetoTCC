from django.urls import path
from .views import *

urlpatterns = [
    path('', CursoListView.as_view(), name="listCurso"),
    path('curso/cria_curso', CursoCreateView.as_view(), name="criaCurso"),
    path('curso/update/<pk>', CursoUpdateView.as_view(), name='updateCurso'),
    path('curso/delete/<pk>', CursoDeleteView.as_view(), name="deleteCurso")
]