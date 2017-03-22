from django.contrib import admin
from .models import Cliente
from .models import Ordenes


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('nombre', 'apellido',)
    prepopulated_fields = {'slug': ('nombre', 'apellido',)}
# Register your models here.
admin.site.register(Cliente, ClienteAdmin)


class OrdenAdmin(admin.ModelAdmin):
    model = Ordenes
    list_display = ('cliente', 'monto', 'tipo',)

# Register your models here.
admin.site.register(Ordenes, OrdenAdmin)