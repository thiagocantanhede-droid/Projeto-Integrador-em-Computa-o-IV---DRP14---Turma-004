from django.contrib import admin

# Register your models here.
from .models import Item, Armario, Usuario, Material, Celular, Notebook

admin.site.register(Usuario)
admin.site.register(Item)
admin.site.register(Armario)
admin.site.register(Material)
admin.site.register(Celular)
admin.site.register(Notebook)