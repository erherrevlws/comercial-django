from django import forms
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from ..models.productos import Productos
from ..models.categoria import Categoria

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    descripcion = forms.CharField(
        max_length=255, required=False,
        label="Descripcion",
        widget=forms.Textarea(attrs={'rows':3}))
    precio_compra = forms.DecimalField(
        max_digits=10, decimal_places=2, label="Precio de compra", min_value=0)
    precio_venta = forms.DecimalField(
            max_digits=10, decimal_places=2, label="Precio de venta", min_value=0)
    stock = forms.IntegerField(label="Stock", min_value=0)
    #generacion de llave forane y carga de datos de la tabla categoria
    categoria =  forms.ModelChoiceField(
        queryset=Categoria.objects.all(), label="Categoria", empty_label="Seleccione una categoria")

    #carga de imagen y validaciones de tipo
    imagen = forms.ImageField(required=False, label="Imagen", validators=[FileExtensionValidator(
        allowed_extensions=["jpg", "png"])])


    def clean(self):
        cleaned_data = super().clean()
        precio_compra = cleaned_data.get('precio_compra')
        precio_venta = cleaned_data.get('precio_venta')
        if precio_compra is not None and precio_venta is not None:
            if precio_venta <= precio_compra:
                self.add_error(
                    'precio_venta',
                    'El precio de venta debe ser mayor que el precio de compra',
                )
        return cleaned_data

    def save(self):
        Productos.objects.create(
            nombre=self.cleaned_data['nombre'],
            descripcion=self.cleaned_data['descripcion'],
            precio_compra= self.cleaned_data['precio_compra'],
            precio_venta=self.cleaned_data['precio_venta'],
            stock=self.cleaned_data['stock'],
            categoria=self.cleaned_data['categoria'],
            imagen=self.cleaned_data.get('imagen', None),
        )

    def update(self, producto):
        imagen_nueva = self.cleaned_data.get('imagen')
        imagen_nombre_anterior = producto.imagen.name
        storage = producto.imagen.storage

        producto.nombre = self.cleaned_data['nombre']
        producto.descripcion = self.cleaned_data['descripcion']
        producto.precio_compra = self.cleaned_data['precio_compra']
        producto.precio_venta = self.cleaned_data['precio_venta']
        producto.stock = self.cleaned_data['stock']
        producto.categoria = self.cleaned_data['categoria']

        #si la imagen es enviada la actualiza porque la imagen no es obligatoria

        if imagen_nueva:
            producto.imagen =  imagen_nueva
        producto.save()

        #valida cuando elimnar la imagen

        if (
            imagen_nueva
            and imagen_nombre_anterior
            and imagen_nombre_anterior != producto.imagen.name
        ):
            #elimina la imagen del servidor
            storage.delete(imagen_nombre_anterior)

