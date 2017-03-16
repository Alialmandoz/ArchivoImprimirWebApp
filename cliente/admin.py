from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('nombre', 'apellido',)
    prepopulated_fields = {'slug': ('nombre', 'apellido',)}
# Register your models here.
admin.site.register(Cliente, ClienteAdmin)