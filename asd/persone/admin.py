from django.contrib import admin
from .models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'datanascita', 'email1', 'cell')
    list_filter = ('stato', 'creato_il', 'modificato_il', 'creatore')
    search_fields = ('cognome', 'nome', 'email1')
    raw_id_fields = ('creatore',)
    ordering = ('stato', 'creato_il')