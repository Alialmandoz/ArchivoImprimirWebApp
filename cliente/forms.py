from cliente.choices import *
from django.forms import ModelForm, SelectDateWidget
import datetime
from django import forms

from openpyxl import *

from cliente.models import Cliente, Ordenes, Trabajo


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'mail', 'telefono', 'direccion')


class OrdenForm(ModelForm):
    fecha_encargo = datetime.date.today
    fecha_entrega = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today() + datetime.timedelta(days=1))

    class Meta:
        model = Ordenes
        fields = ('fecha_entrega',)

        def __init__(self):
            self.fields('fecha_entrega',)


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


class BuscarOrdenForm(forms.Form):
    # cliente = forms.CharField()
    fecha1 = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today())
    fecha2 = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today())
    # tipo = forms.CharField(widget=forms.Select(choices=TIPO_TRABAJO))
    # cantidad = forms.IntegerField()

    # impresion = forms.CharField(widget=forms.Select(choices=HOJA))
    # blanco_y_negro = forms.MultipleChoiceField(required=False, widget=forms.CheckboxInput, choices=BYN)