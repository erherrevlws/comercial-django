from django.db import models

class TipoPago(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre