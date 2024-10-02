from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class AttivoManager(models.Manager):
    def get_queryset(self):
        return super(AttivoManager,
                     self).get_queryset()\
                        .filter(stato='attivo')


class Persona(models.Model):
    STATUS_CHOICES = (
        ('disattivo', 'Disattivo'),
        ('attivo', 'Attivo'),
        ('sospeso', 'Sospeso'),
    )
    SESSO_CHOICES = (
        ('m', 'M'),
        ('f', 'F'),
    )
    stato = models.CharField(max_length=16, choices=STATUS_CHOICES, default='attivo')
    nome = models.CharField(max_length=128)
    cognome = models.CharField(max_length=128)
    sesso = models.CharField(max_length=2, choices=SESSO_CHOICES, default='m')
    datanascita = models.DateField(null=True, blank=True)
    comunenascita = models.CharField(max_length=128, null=True, blank=True)
    codicefiscale = models.CharField(max_length=32, null=True, blank=True)
    entetessera = models.CharField(max_length=128, null=True, blank=True)
    codicetessera = models.CharField(max_length=64, null=True, blank=True)
    datariltessera = models.DateField(null=True, blank=True)
    indirizzo = models.CharField(max_length=250, null=True, blank=True)
    comune = models.CharField(max_length=250, null=True, blank=True)
    tel = models.CharField(max_length=64, null=True, blank=True)
    cell = models.CharField(max_length=64, null=True, blank=True)
    email1 = models.CharField(max_length=128, null=True, blank=True)
    email2 = models.CharField(max_length=128, null=True, blank=True)
    creato_il = models.DateTimeField(auto_now_add=True)
    modificato_il = models.DateTimeField(auto_now=True)
    note = models.TextField(null=True, blank=True)
    creatore = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='persone')

    class Meta:
        ordering = ('cognome',)

    def __str__(self):
        return f"{self.cognome} {self.nome}"
    
    objects = models.Manager()
    attivo = AttivoManager()