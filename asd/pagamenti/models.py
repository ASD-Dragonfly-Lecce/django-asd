from django.db import models
from django.contrib.auth.models import User
from persone.models import Persona


class BaseModel(models.Model):
    eliminato = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.eliminato = True
        self.save()


class Conto(models.Model):
    codice = models.CharField(max_length=16)
    descrizione = models.CharField(max_length=128)


class Pagamento(BaseModel):
    pagante = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='pagamenti')
    data = models.DateField("Data")
    data_contabile = models.DateField("Data Contabile", blank=True, null=True)
    descrizione = models.CharField(max_length=255)
    entrate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    entrate_int = models.IntegerField(default=0)
    uscite = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    uscite_int = models.IntegerField(default=0)
    riferimento_documento = models.CharField(max_length=32, blank=True)
    riga = models.PositiveIntegerField(default=1)
    anagrafica = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True)
    codice = models.CharField(max_length=128, blank=True)
    creato_il = models.DateTimeField(auto_now_add=True)
    modificato_il = models.DateTimeField(auto_now=True)
    utente = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)