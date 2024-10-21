from django.contrib import admin
from .models import Notizia


@admin.register(Notizia)
class NotiziaAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'creato_il')
    list_filter = ('titolo', 'creato_il', 'modificato_il')
    search_fields = ('titolo', 'data')
    raw_id_fields = ('utente',)
    ordering = ('titolo', 'creato_il')