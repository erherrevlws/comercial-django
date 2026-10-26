from django.shortcuts import render, redirect, get_object_or_404
from catalogo.models.rol import Rol
from catalogo.forms.rol_form import RolForm

def lista_roles(request):
    return render(request, "rol/lista.html", {'roles': Rol.objects.all()})

def delete_rol(request, id):
    get_object_or_404(Rol, id=id).delete()
    return redirect('list_rol')

def add_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_rol')
    else:
        form = RolForm()
    return render(request, "rol/add.html", {'form': form})

def update_rol(request, id):
    rol = get_object_or_404(Rol, id=id)
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.update(rol)
            return redirect('list_rol')
    else:
        form = RolForm(initial={'nombre': rol.nombre, 'descripcion': rol.descripcion})
    return render(request, "rol/update.html", {'form': form, 'rol': rol})