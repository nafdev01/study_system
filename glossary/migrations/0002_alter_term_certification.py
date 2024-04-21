# Generated by Django 5.0.4 on 2024-04-17 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0001_initial'),
        ('notes', '0002_remove_domain_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='certification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='notes.certification'),
        ),
    ]
