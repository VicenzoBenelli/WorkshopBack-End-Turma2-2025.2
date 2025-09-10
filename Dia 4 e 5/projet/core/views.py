import requests
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView
from .models import Endereco
from .forms import EnderecoForm


class EnderecoFormView(FormView):
    template_name = 'endereco_form.html'
    form_class = EnderecoForm
    success_url = reverse_lazy('endereco_list')

    def form_valid(self, form):
        cep = form.cleaned_data['cep'].replace('-', '').strip()

        
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/',verify=False)

        if response.status_code == 200:
            data = response.json()

            
            if not data.get('erro'):
                
                if not Endereco.objects.filter(cep=data.get('cep')).exists():
                    Endereco.objects.create(
                        cep=data.get('cep'),
                        rua=data.get('logradouro'),
                        bairro=data.get('bairro'),
                        cidade=data.get('localidade'),
                        estado=data.get('uf'),
                    )

        return super().form_valid(form)


class EnderecoListView(ListView):
    model = Endereco
    template_name = 'endereco_list.html'
    context_object_name = 'enderecos'


class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = 'endereco_detail.html'
    context_object_name = 'endereco'


class EnderecoUpdateView(UpdateView):
    model = Endereco
    fields = ['cep', 'rua', 'bairro', 'cidade', 'estado']
    template_name = 'endereco_update.html'
    success_url = reverse_lazy('endereco_list')


class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'endereco_confirm_delete.html'
    success_url = reverse_lazy('endereco_list')
