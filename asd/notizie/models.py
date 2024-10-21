from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


class Notizia(models.Model):
    STATUS_CHOICES = (
        ('bozza', 'Bozza'),
        ('pubblicata', 'Pubblicata'),
    )
    titolo = models.CharField(max_length=255)
    slug = models.CharField(max_length=250, unique_for_date='creato_il', blank=True, null=True)
    corpo = models.TextField()
    creato_il = models.DateTimeField(auto_now_add=True)
    modificato_il = models.DateTimeField(auto_now=True)
    utente = models.ForeignKey(User,
                               null=True,
                               on_delete=models.CASCADE)
    class Meta:
        ordering = ('-creato_il',)
        verbose_name_plural = "notizie"

    def __str__(self):
        creato_il = self.creato_il.strftime("%d/%m/%Y %H:%M")
        return f"{creato_il} - {self.titolo}"
