from django import forms
from catalogo.models.tipoPago import TipoPago

class TipoPagoForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", required=True)
    descripcion = forms.CharField(max_length=255, label="Descripción", required=False, widget=forms.Textarea(attrs={"rows": 3}))

    def save(self):
        TipoPago.objects.create(
            nombre=self.cleaned_data['nombre'],
            descripcion=self.cleaned_data['descripcion']
        )

    def update(self, tipo_pago):
        tipo_pago.nombre = self.cleaned_data['nombre']
        tipo_pago.descripcion = self.cleaned_data['descripcion']
        tipo_pago.save()