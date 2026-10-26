from django.db import models

class Categoria(models.Model):

    nombre = models.CharField(max_length=255, verbose_name='Nombre')

    descripcion = models.TextField(
        max_length=255, null=True, verbose_name='Descripción')

    created_at = models.DateTimeField(verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(verbose_name='Fecha de actualización')


    def __str__(self):
        return self.nombre