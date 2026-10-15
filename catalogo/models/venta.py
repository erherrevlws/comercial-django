from django.db import models
from .cliente import Cliente 
from .usuario import Usuario
from .tipoPago import TipoPago

class Venta(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha de venta")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='ventas', verbose_name="Cliente"
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='ventas', verbose_name="Usuario"
    )
    tipo_pago = models.ForeignKey(
        TipoPago, on_delete=models.CASCADE, related_name='ventas', verbose_name="Tipo de pago"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return f"Venta #{self.id} - Total: {self.total}"
