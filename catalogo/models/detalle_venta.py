from django.db import models
from .venta import Venta
from .productos import Productos

class DetalleVenta(models.Model):
    venta = models.ForeignKey(
        Venta, on_delete=models.CASCADE, related_name='detalles', verbose_name="Venta"
    )
    producto = models.ForeignKey(
        Productos, on_delete=models.CASCADE, related_name='detalles_venta', verbose_name="Producto"
    )
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio unitario")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"Detalle Venta #{self.venta.id} - Producto: {self.producto.nombre} (x{self.cantidad})"