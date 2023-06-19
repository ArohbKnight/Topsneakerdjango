# Generated by Django 4.2.1 on 2023-06-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.RemoveField(
            model_name='marca',
            name='id_marca',
        ),
        migrations.RemoveField(
            model_name='modelo',
            name='nombre_modelo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='detalle',
        ),
        migrations.DeleteModel(
            name='Foto',
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.DeleteModel(
            name='Modelo',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]