from django.urls import path
from .views import (
    EnderecoFormView, EnderecoListView, EnderecoDetailView,
    EnderecoUpdateView, EnderecoDeleteView
)

urlpatterns = [
    path('', EnderecoFormView.as_view(), name='endereco_form'),
    path('lista/', EnderecoListView.as_view(), name='endereco_list'),
    path('detalhe/<int:pk>/', EnderecoDetailView.as_view(), name='endereco_detail'),
    path('editar/<int:pk>/', EnderecoUpdateView.as_view(), name='endereco_update'),
    path('deletar/<int:pk>/', EnderecoDeleteView.as_view(), name='endereco_delete'),
]
