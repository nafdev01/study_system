# Generated by Django 4.2.11 on 2024-04-19 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='MyEvent',
        ),
        migrations.AlterModelOptions(
            name='myevent',
            options={'ordering': ['added_on'], 'verbose_name': 'MyEvent', 'verbose_name_plural': 'MyEvents'},
        ),
    ]
