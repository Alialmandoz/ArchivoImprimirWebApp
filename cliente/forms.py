from cliente.choices import *
from django.forms import ModelForm
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django import forms

from openpyxl import *

from cliente.models import Cliente, Ordenes, Trabajo


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'mail', 'telefono', 'direccion')


class OrdenForm(ModelForm):
    fecha_encargo = datetime.date.today
    fecha_entrega = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today)

    class Meta:
        model = Ordenes
        fields = ()


class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = ('tipo', 'detalle', 'monto', 'adelanto', 'saldo')


class Calculador(forms.Form):
    cantidad = forms.IntegerField(required=True)
    soporte = forms.CharField(widget=forms.Select(choices=SOPORTE))
    impresion = forms.CharField(widget=forms.Select(choices=HOJA))
    blanco_y_negro = forms.MultipleChoiceField(required=False, widget=forms.CheckboxInput, choices=BYN)

    def calcular(self, material, cantidad, caras):
        if 1 <= cantidad <= 4:
            cant = '2'
        elif 5 <= cantidad <= 10:
            cant = '3'
        elif 11 <= cantidad <= 50:
            cant = '4'
        elif 51 <= cantidad <= 100:
            cant = '5'
        elif 101 <= cantidad <= 250:
            cant = '6'
        else:
            cant = '7'

        if int(caras[0]) > 1:
            material = (chr(ord(material) + 1))
        cell = str(str(material) + str(cant))
        lista = load_workbook('cliente/static/pdf/lista.xlsx')
        precio = lista['lista'][cell].value
        return "{:10.2f}".format(precio * cantidad)