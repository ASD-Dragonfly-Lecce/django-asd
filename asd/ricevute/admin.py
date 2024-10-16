from django.contrib import admin
from .models import Ricevuta


@admin.register(Ricevuta)
class RicevutaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'data')
    list_filter = ('numero', 'creato_il', 'modificato_il')
    search_fields = ('numero', 'data')
    raw_id_fields = ('persona',)
    ordering = ('numero', 'creato_il')