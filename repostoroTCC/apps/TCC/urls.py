from django.urls import path
from .views import TCCListView, TCCUploadView, TCCUpdateView, TCCDeleteView

urlpatterns = [
    path('', TCCListView.as_view(), name="listTCC"),
    path('tcc/cria_tcc', TCCUploadView, name="criaTCC"),
    path('tcc/update/<pk>', TCCUpdateView.as_view(), name='updateTCC'),
    path('tcc/delete/<pk>', TCCDeleteView.as_view(), name="deleteTCC")
]