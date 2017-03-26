from django.forms import ModelForm
from cliente.models import Cliente, Ordenes


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'mail', 'telefono', 'direccion',)


class OrdenForm(ModelForm):
    class Meta:
        model = Ordenes
        fields = ('cliente', 'monto', 'tipo')