# Generated by Django 5.1.1 on 2024-10-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persone', '0007_allegato'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='certmedico_scadenza',
            field=models.DateField(blank=True, null=True),
        ),
    ]
