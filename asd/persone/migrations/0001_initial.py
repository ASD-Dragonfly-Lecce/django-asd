# Generated by Django 5.1.1 on 2024-10-01 21:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('cognome', models.CharField(max_length=128)),
                ('sesso', models.CharField(choices=[('m', 'M'), ('f', 'F')], default='m', max_length=2)),
                ('datanascita', models.DateField()),
                ('comunenascita', models.CharField(max_length=128)),
                ('codicefiscale', models.CharField(max_length=32)),
                ('entetessera', models.CharField(max_length=128)),
                ('codicetessera', models.CharField(max_length=64)),
                ('datariltessera', models.DateField()),
                ('indirizzo', models.CharField(max_length=250)),
                ('comune', models.CharField(max_length=250)),
                ('tel', models.CharField(max_length=64)),
                ('cell', models.CharField(max_length=64)),
                ('email1', models.CharField(max_length=128)),
                ('email2', models.CharField(max_length=128)),
                ('creato_il', models.DateTimeField(auto_now_add=True)),
                ('modificato_il', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('creatore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persone', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('cognome',),
            },
        ),
    ]
