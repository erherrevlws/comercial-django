from django import forms
from catalogo.models.rol import Rol

class RolForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", required=True)
    descripcion = forms.CharField(max_length=255, label="Descripción", required=False, widget=forms.Textarea(attrs={"rows": 3}))

    def save(self):
        Rol.objects.create(
            nombre=self.cleaned_data['nombre'],
            descripcion=self.cleaned_data['descripcion']
        )

    def update(self, rol):
        rol.nombre = self.cleaned_data['nombre']
        rol.descripcion = self.cleaned_data['descripcion']
        rol.save()