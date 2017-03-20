from django.forms import ModelForm
from cliente.models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido',)