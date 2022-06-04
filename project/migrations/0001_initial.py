# Generated by Django 4.0.3 on 2022-04-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customercheckout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_room_num', models.CharField(max_length=100)),
                ('customer_room_type', models.CharField(max_length=100)),
                ('customer_citizenship', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_checkin', models.CharField(max_length=100)),
                ('customer_checkout', models.CharField(max_length=100)),
                ('customer_roomprice', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=100)),
                ('customer_totalamount', models.CharField(max_length=100)),
                ('customer_booked_date', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Receipt',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('image', models.FileField(upload_to='item_images')),
                ('itemname', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='OrderedFoodItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_orderitem', models.CharField(max_length=100)),
                ('customer_tablenum', models.CharField(blank=True, max_length=100)),
                ('customer_roomnum', models.CharField(blank=True, max_length=100)),
                ('customer_itemprice', models.CharField(max_length=100)),
                ('customer_ordertime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'foods',
            },
        ),
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ordereditem', models.CharField(max_length=100)),
                ('tablenum', models.CharField(blank=True, max_length=100)),
                ('roomnum', models.CharField(blank=True, max_length=100)),
                ('itemprice', models.CharField(max_length=100)),
                ('ordertime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='RoomBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('room_type', models.CharField(max_length=100)),
                ('room_num', models.CharField(max_length=100)),
                ('checkin', models.CharField(max_length=200)),
                ('checkout', models.CharField(max_length=200)),
                ('room_price', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('citizenship', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('booked_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'roombook',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=200)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
    ]
