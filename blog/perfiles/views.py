from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm


@login_required
def perfil(request):
    user = request.user
    context = {'user': user}
    return render(request, 'perfiles/perfil.html', context)

@login_required
def editarPerfil(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return render(request, 'perfiles/perfil.html', {'form': form})
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'perfiles/editarPerfil.html', {'form': form})