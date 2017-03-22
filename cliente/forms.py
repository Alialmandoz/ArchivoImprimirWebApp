from django.forms import ModelForm
from cliente.models import Cliente, Ordenes


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido',)


class OrdenForm(ModelForm):
    class Meta:
        model = Ordenes
        fields = ('tipo', 'monto', 'cliente')