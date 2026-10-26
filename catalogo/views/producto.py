from django.shortcuts import render, redirect, get_object_or_404
from ..models.productos import Productos
from ..forms.producto_form import ProductoForm
from django.core.paginator import Paginator

def lista_productos(request):
    productos = Productos.objects.all().order_by('id')
    paginator = Paginator(productos, 10)

    pagina = request.GET.get('page')
    productos_paginados = paginator.get_page(pagina)

    return render(request, "producto/lista.html", context={
        'productos': productos_paginados
    })

def delete_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    if producto.imagen: 
        producto.imagen.storage.delete(producto.imagen.name)
    producto.delete()
    return redirect('list_producto')

def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_producto')
        else: 
            return render(request, "producto/add.html", context={
                'form': form
            })
    return render(request, "producto/add.html", context={
        'form': ProductoForm()
    })

def update_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.update(producto)
            return redirect('list_producto')
        else:
            return render(request, "producto/update.html", context={
                'form' : form
            })


    form = ProductoForm(initial={
        'nombre': producto.nombre,
        'descripcion' : producto.descripcion,
        'precion_compra' : producto.precio_compra,
        'precio_venta' : producto.precio_venta,
        'stock': producto.stock,
        'categoria': producto.categoria,
        'imagen' : producto.imagen
    })

    return render(request, "producto/update.html", context={
        'form': form,
        'producto': producto
    })
