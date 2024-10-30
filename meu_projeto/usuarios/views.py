from django.shortcuts import render, redirect
from .forms import UsuarioForm  # Supondo que você tenha um formulário chamado UsuarioForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona para a página de sucesso
    else:
        form = UsuarioForm()

    return render(request, 'usuarios/registrar_usuario.html', {'form': form})

def sucesso(request):
    return render(request, 'usuarios/sucesso.html')  # Renderiza a página de sucesso
