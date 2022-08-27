from django.urls import path
from .views import *

urlpatterns = [
    path('', OrientadorListView.as_view(), name="listOrientador"),
    path('cria_orientador', OrientadorCreateView.as_view(), name="criaOrientador"),
    path('update/<pk>', OrientadorUpdateView.as_view(), name='updateOrientador'),
    path('delete/<pk>', OrientadorDeleteView.as_view(), name="deleteOrientador")
]