from django.shortcuts import redirect, render
from .models import Pessoa
from .forms import PessoaForm



def lista_pessoas(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'lista_pessoas.html', {'pessoas': pessoas})

def nova_pessoa(request):
    if request.method == 'POST':  
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'nova_pessoa.html', {'form': form})  
