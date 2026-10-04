from django.shortcuts import render

# Create your views here.
def lista_categorias(request):
    listado_categorias = [
        {
            'id': 1,
            'nombre': 'tv',
            'descripcion': 'Televisores de alta gama',
        },
        {
            'id': 2,
            'nombre': 'Laptop',
            'descripcion': 'Computadoras portatiles',
        }
        
    ]
    return render(request, "categoria/lista.html", context={
        'categorias': listado_categorias
    })