# Generated by Django 4.0.3 on 2022-04-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_roombook_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombook',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]