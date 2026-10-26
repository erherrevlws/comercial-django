from django.shortcuts import render, redirect, get_object_or_404
from catalogo.models.cliente import Cliente
from catalogo.forms.cliente_form import ClienteForm

def lista_clientes(request):
    return render(request, "cliente/lista.html", {'clientes': Cliente.objects.all()})

def delete_cliente(request, id):
    get_object_or_404(Cliente, id=id).delete()
    return redirect('list_cliente')

def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_cliente')
    else:
        form = ClienteForm()
    return render(request, "cliente/add.html", {'form': form})

def update_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.update(cliente)
            return redirect('list_cliente')
    else:
        form = ClienteForm(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'telefono': cliente.telefono, 'correo': cliente.correo, 'direccion': cliente.direccion})
    return render(request, "cliente/update.html", {'form': form, 'cliente': cliente})