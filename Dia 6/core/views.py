from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import viewsets
from .models import Address
from .serializers import AddressSerializer

# API REST
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

# Página inicial redireciona para a API
def home(request):
    return redirect('/addresses/')

# Rota de teste simples
def teste(request):
    return HttpResponse("Rota de teste funcionando!")
