from django.shortcuts import redirect, render
from .models import Pessoa
from .forms import PessoaForm

def menu(request):
    return render(request, 'menu.html')

def lista_pessoas(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'lista_pessoas.html', {'pessoas': pessoas})

def nova_pessoa(request):
    if request.method == 'POST':  
        form = PessoaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'nova_pessoa.html', {'form': form})  

def editar_pessoa(request, id):
    pessoa = Pessoa.objects.get(id = id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid:
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'editar_pessoa.html', {'form': form})

def excluir_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('lista_pessoas')
    return render(request, 'excluir_pessoa.html', {'pessoa': pessoa})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            pessoa = Pessoa.objects.get(email=email)
            if pessoa.senha == senha:
                # Autenticação bem-sucedida
                return redirect('menu')  # ou outra URL
            else:
                erro = 'Senha incorreta'
        except Pessoa.DoesNotExist:
            erro = 'Usuário não encontrado'

        return render(request, 'login.html', {'erro': erro})

    return render(request, 'login.html')