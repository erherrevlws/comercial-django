from django import forms
from catalogo.models.cliente import Cliente

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", required=True)
    apellido = forms.CharField(max_length=100, label="Apellido", required=True)
    telefono = forms.CharField(max_length=9, label="Teléfono", required=True)
    correo = forms.EmailField(max_length=150, label="Correo", required=False)
    direccion = forms.CharField(max_length=255, label="Dirección", required=False, widget=forms.Textarea(attrs={"rows": 3}))

    def save(self):
        Cliente.objects.create(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data['telefono'],
            correo=self.cleaned_data['correo'],
            direccion=self.cleaned_data['direccion']
        )

    def update(self, cliente):
        cliente.nombre = self.cleaned_data['nombre']
        cliente.apellido = self.cleaned_data['apellido']
        cliente.telefono = self.cleaned_data['telefono']
        cliente.correo = self.cleaned_data['correo']
        cliente.direccion = self.cleaned_data['direccion']
        cliente.save()