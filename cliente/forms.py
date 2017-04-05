from cliente.choices import *
from django.forms import ModelForm
from cliente.models import Cliente, Ordenes
from django import forms

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'mail', 'telefono', 'direccion',)


class OrdenForm(ModelForm):
    class Meta:
        model = Ordenes
        fields = ('cliente', 'tipo', 'detalle', 'monto', 'entrega', 'saldo')


BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'), ('green', 'Green'), ('black', 'Black'),)


class Calculador(forms.Form):
    soporte = forms.CharField(max_length=3, widget=forms.Select(choices=SOPORTE))
    impresion = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=HOJA)
    cantidad  = forms.IntegerField()
    byn = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=BYN)