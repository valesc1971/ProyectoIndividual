# Generated by Django 4.0.4 on 2022-05-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0012_delete_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='receive_newsletter',
            field=models.BooleanField(default=False, null=True),
        ),
    ]