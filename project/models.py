from django.db import models


# Create your models here.
class Staff(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    last_login = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "staff"


# Create your models here.
class RoomBook(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100)
    room_num = models.CharField(max_length=100)
    checkin = models.CharField(max_length=200)
    checkout = models.CharField(max_length=200)
    room_price = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    booked_date = models.DateTimeField(auto_now_add=True)
    check_out_status = models.BooleanField(default=False)

    class Meta:
        db_table = "roombook"


# Create your models here.
class Food(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    image = models.FileField(upload_to='item_images')
    itemname = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)

    class Meta:
        db_table = "menu"


# Create your models here.
class customercheckout(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    customer_room_num = models.CharField(max_length=100)
    customer_room_type = models.CharField(max_length=100)
    customer_citizenship = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_checkin = models.CharField(max_length=100)
    customer_checkout = models.CharField(max_length=100)
    customer_roomprice = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    totalamount = models.CharField(max_length=100)
    customer_booked_date = models.CharField(max_length=100)


    class Meta:
        db_table = "Receipt"


# Create your models here.
class OrderedItems(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    ordereditem = models.CharField(max_length=100)
    tablenum = models.CharField(max_length=100,blank=True )
    roomnum = models.CharField(max_length=100,blank=True )
    itemprice = models.CharField(max_length=100)
    ordertime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"

# Create your models here.
class OrderedFoodItems(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    customer_orderitem = models.CharField(max_length=100)
    customer_tablenum = models.CharField(max_length=100,blank=True )
    customer_roomnum = models.CharField(max_length=100,blank=True )
    customer_itemprice = models.CharField(max_length=100)
    customer_ordertime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "foods"
