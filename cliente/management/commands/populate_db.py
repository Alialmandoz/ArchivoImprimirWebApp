import random

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from openpyxl import *
from cliente.models import Cliente


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('clientes', type=int)

    def _crear_cliente(self, num_clientes):

        """
        arguments: num_clientes int

        load a num_clientes numbrer of Clientes instances in to the database

        the data is collected from a xlsx file in the pdf static folder through
        openpyxl library.

        """
        help = 'load a num_clientes number of clients instances in to the data base'
        print('cargando {0} clientes en la base de datos'.format(num_clientes))
        db_cli = []
        for cliente in Cliente.objects.all():
            db_cli.append(cliente.slug)

        for __ in range(num_clientes):
            row = random.randrange(1, 119)
            lista = load_workbook(filename='cliente/static/pdf/contactos.xlsx', read_only=True)

            cliente = Cliente(nombre=lista['contactos']['a' + str(row)].value,
                              apellido=lista['contactos']['b' + str(row)].value,
                              mail=lista['contactos']['e' + str(row)].value,
                              telefono=lista['contactos']['d' + str(row)].value,
                              direccion=lista['contactos']['c' + str(row)].value,
                              slug=slugify(lista['contactos']['a' + str(row)].value + '-' +
                                           lista['contactos']['b' + str(row)].value),
                              )
            if cliente.slug in db_cli:
                print(cliente.slug + ': cliente en lista')

            else:
                cliente.save()
                print(cliente.nombre, cliente.apellido, cliente.slug, " agregado")

    def handle(self, *args, **options):
        clientes = options['clientes']
        self._crear_cliente(clientes)