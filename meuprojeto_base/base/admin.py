from django.contrib import admin

# Register your models here.
from .models import Item, Armario, Tamanho, Usuario

admin.site.register(Usuario)
admin.site.register(Item)
admin.site.register(Armario)
admin.site.register(Tamanho)