# Generated by Django 5.0.4 on 2024-04-21 00:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0002_alter_term_certification'),
        ('notes', '0002_remove_domain_overview'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certification',
            new_name='Course',
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['abbreviation'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
    ]