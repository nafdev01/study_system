# Generated by Django 4.2.11 on 2024-04-19 03:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('event_on', models.DateField()),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('SC', 'Sucess'), ('DG', 'Danger'), ('IN', 'Info'), ('PN', 'Pink'), ('PR', 'Primary'), ('WR', 'Warning')], default='IN', max_length=2)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['added_on'],
            },
        ),
    ]
