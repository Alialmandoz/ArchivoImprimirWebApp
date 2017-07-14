from ali.models import Mensaje
from django.forms import ModelForm


class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = ('nombre', 'mail', 'telefono', 'texto')
