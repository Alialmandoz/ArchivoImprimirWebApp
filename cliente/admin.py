from django.contrib import admin
from .models import Ordenes, Trabajo, Cliente


class OrdenesInline(admin.TabularInline):
    model = Ordenes
    extra = 0


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('nombre', 'apellido',)
    prepopulated_fields = {'slug': ('nombre', 'apellido',)}
    inlines = [OrdenesInline]
    search_fields = ['slug']
# Register your models here.
admin.site.register(Cliente, ClienteAdmin)


class OrdenAdmin(admin.ModelAdmin):
    model = Ordenes
    list_display = ('cliente', 'fecha_encargo', 'fecha_entrega')

# Register your models here.
admin.site.register(Ordenes, OrdenAdmin)


class TrabajoAdmin(admin.ModelAdmin):
    model = Trabajo
    list_display = ('pk', 'tipo', 'detalle', 'monto', 'adelanto', 'saldo', 'orden',)


# Register your models here.
admin.site.register(Trabajo, TrabajoAdmin)
