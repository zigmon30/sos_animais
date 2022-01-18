from django.contrib import admin
from .models import Animal

# Register your models here.

#admin.site.register(PetLost)
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'cidade', 'usuario', 'descricao',]
