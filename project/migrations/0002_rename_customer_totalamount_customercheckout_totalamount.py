# Generated by Django 4.0.3 on 2022-04-01 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customercheckout',
            old_name='customer_totalamount',
            new_name='totalamount',
        ),
    ]
