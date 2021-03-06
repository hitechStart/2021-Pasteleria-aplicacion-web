# Generated by Django 3.2.7 on 2021-09-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_pasteleria_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desayuno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='pasteleria', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
        ),
    ]
