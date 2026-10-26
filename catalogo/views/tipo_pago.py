from django.shortcuts import render, redirect, get_object_or_404
from catalogo.models.tipoPago import TipoPago
from catalogo.forms.tipo_pago_form import TipoPagoForm

def lista_tipo_pago(request):
    return render(request, "tipo_pago/lista.html", {'tipos': TipoPago.objects.all()})

def delete_tipo_pago(request, id):
    get_object_or_404(TipoPago, id=id).delete()
    return redirect('list_tipo_pago')

def add_tipo_pago(request):
    if request.method == 'POST':
        form = TipoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tipo_pago')
    else:
        form = TipoPagoForm()
    return render(request, "tipo_pago/add.html", {'form': form})

def update_tipo_pago(request, id):
    tipo_pago = get_object_or_404(TipoPago, id=id)
    if request.method == 'POST':
        form = TipoPagoForm(request.POST)
        if form.is_valid():
            form.update(tipo_pago)
            return redirect('list_tipo_pago')
    else:
        form = TipoPagoForm(initial={'nombre': tipo_pago.nombre, 'descripcion': tipo_pago.descripcion})
    return render(request, "tipo_pago/update.html", {'form': form, 'tipo_pago': tipo_pago})