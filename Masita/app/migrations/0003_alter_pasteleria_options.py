# Generated by Django 3.2.7 on 2021-09-28 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_pasteleria_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pasteleria',
            options={'ordering': ['created'], 'verbose_name': 'receta', 'verbose_name_plural': 'recetas'},
        ),
    ]