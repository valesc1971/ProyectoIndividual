# Generated by Django 4.0.4 on 2022-05-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0010_remove_usuario_clave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
