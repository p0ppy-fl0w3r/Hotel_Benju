import email

from django.contrib import auth
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from flask import Request



# Create your views here.
from project.forms import StaffForm, FoodForm, OrderForm, RoomForm, customercheckoutForm, OrderedFoodItemsForm
from project.models import Staff, RoomBook, Food, OrderedItems, customercheckout, OrderedFoodItems


def home(request):  # login page

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            if Staff is not None:
                staff = Staff.objects.get(username=username, password=password)
                return redirect('MainHome')

        except:
            user = auth.authenticate(request, username=username, password=password)
            # messages.error(request,"Invalid credentials")
            if user is not None:
                return redirect('show/')
            return render(request, 'login.html',{"error_message":"Invalid Credentials!!"})

    else:
        print("Log In successfully")
        form = StaffForm()
        return render(request, "login.html", {'form': form})


def show(request):
    return render(request, "dashboard.html")


def food(request):
    return render(request, "menue.html")


def MainHome(request):
    return render(request, "services.html" ,{'ro': RoomBook.objects.exclude(check_out_status=True)})



def signup(request):
    context = {'success': False}
    if request.method == "POST":
        form = StaffForm(request.POST)
        form.save()
        context = {'success': True}
    return render(request, "registerstaff.html" , context )


def room_booked(request):
    # context = {'success': False}
    ro = RoomBook.objects.exclude(check_out_status=True)
    rom_count = ro.count()
    # rm_num = RoomBook.objects.get('room_num')
    room_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    if request.method == "POST":
         
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        room_type = request.POST['room_type']
        room_num = request.POST['room_num']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        room_price = request.POST['room_price']
        phone = request.POST['phone']
        email = request.POST['email']
        citizenship = request.POST['citizenship']
        print(checkin)
        print(checkout)
        # if (rm_num == room_num):
            
        #     return render(request, "customer-detaling.html", {'ro': ro},{'error_message':'this room is already book!'})
        # elif (room_num <= 30):
        #     return render(request, "customer-detaling.html", {'ro': ro},{'error_message':'this room is already book!'})
        # else:
        
        if rom_count <= 30:
            if int(room_num) in room_list:
                try:
                    get_room = RoomBook.objects.get(room_num=room_num)
                    if get_room.check_out_status == True:

                        get_room.firstname = firstname
                        get_room.lastname = lastname
                        get_room.address = address
                        get_room.room_type = room_type
                        get_room.room_num = room_num
                        get_room.checkin=checkin
                        get_room.checkout=checkout
                        get_room.room_price=room_price
                        get_room.phone=phone
                        get_room.email=email
                        get_room.citizenship=citizenship
                        get_room.check_out_status = False                        
                        get_room.save()
                        context = {'success': True, 'ro': ro,}
                        return render(request, "customer-detaling.html", context)
                    else:
                        context = {'success': False, 'ro': ro, 'message': 'Room already booked'}
                        return render(request, "customer-detaling.html", context)
                except:                
                    ins = RoomBook(firstname=firstname, lastname=lastname, address=address, room_type=room_type, room_num=room_num,
                                checkin=checkin,
                                checkout=checkout, room_price=room_price, phone=phone, email=email, citizenship=citizenship)
                    ins.save()
                    context = {'success': True, 'ro': ro,}
                    return render(request, "customer-detaling.html", context)
            else:
                context = {'success': False, 'ro': ro, 'message': 'Room not available'}
                return render(request, "customer-detaling.html", context)
        else:
            context = {'success': False, 'ro': ro, 'message': 'Out of rooms'}
            return render(request, "customer-detaling.html", context)

        print("data is created on db")
    context = {'ro': ro,}
    return render(request, "customer-detaling.html", context)


def signout(request):
    request.session.clear()
    print("Logged Out Successfully!!")
    return redirect('home')


def delete_staff(request, P_id):
    con = Staff.objects.get(id=P_id)
    con.delete()
    print("delete successfully")
    return redirect("showstaffs")


def delete_book(request, P_id):
    # messages.success(request,"Sucessfully deleted")
    con = customercheckout.objects.get(id=P_id)
    con.delete()
    print("delete successfully")
    return redirect("/showbookedrooms" ) 


def delete_roombook(request, P_id):
    con = RoomBook.objects.get(id=P_id)
    con.delete()
    print("delete successfully")
    return redirect("/roomstatement")


def checkout(request, P_id):
    return redirect("/showbookedrooms")


def OrderServed(request, P_id):
    con = OrderedItems.objects.get(id=P_id)
    con.delete()
    return redirect("/roomstatement")


def orderconfirm(request):
    if request.method == "POST":
        print(request.POST)
        form = OrderedFoodItemsForm(request.POST, request.FILES)
        form.save()
        print("Order Saved")
        return render(request, "roomstatement.html",{"success":True},)
    else:
        form = RoomForm()
        FoodForm()
    return render(request, "roomstatement.html")


def delete_item(request, P_id):
    con = Food.objects.get(id=P_id)
    con.delete()
    print("delete successfully")
    return redirect("/showmenu", {"error_message":"Deleted Successfully"})


def delete_foodadmin(request, P_id):
    con = OrderedFoodItems.objects.get(id=P_id)
    con.delete()
    print("delete successfully")
    return redirect("foodorders")


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = Staff.objects.filter(fullname__contains=searched)
        searchroom = customercheckout.objects.filter(customer_name__contains=searched)
        return render(request, "room.html", {'searched': searched, 'items': items, 'searchroom': searchroom})
    else:
        search_param = request.GET['searched']
        return render(request, "room.html")


def searchitem(request):
    return redirect("showbookedrooms")


def ordered(request):
    return render(request, "ordered.html")


def add(request):
    return render(request, "additems.html")


def create_items(request):
    context = {'success': False}
    if request.method == "POST":
        print(request.POST)
        form = FoodForm(request.POST, request.FILES)
        form.save()
        print("Item created")
        context = {'success': True}
    return render(request, "additems.html", context)


def menu(request):
    m = Food.objects.all()
    u = Staff.objects.all()
    context = {'success': False}
    if request.method == "POST":

        print(request.POST)
        form = OrderForm(request.POST, request.FILES)
        form.save()
        print("Item Ordered")

        return  render(request, "menue.html", {'menu': m, 'form': form, "name": u, 'success': True})
    else:
        form = FoodForm()
        FoodForm()
        context = {'success': True}

    return render(request, "menue.html", {'menu': m, 'form': form, "name": u})


def create(request):
    return render(request, 'additems.html')


def showbookedrooms(request, search_param):
        rooms = customercheckout.objects.filter(customer_name = search_param)
        return render(request, "room.html", {'rooms': rooms, })


def showAllrooms(request):
    rooms = customercheckout.objects.all()
    return render(request, "room.html", {'rooms': rooms, })

def foodorders(request):
    order = OrderedFoodItems.objects.all()
    return render(request, 'orderedFood.html', {'orders': order})


def showmenu(request):
    foods = Food.objects.all()
    return render(request, 'menuitems.html', {'foods': foods})


def showstaffs(request):
    staff = Staff.objects.all()
    return render(request, 'staff.html', {'staff': staff})


def roomstatement(request):
    room = RoomBook.objects.exclude(check_out_status=True)
    foods = OrderedItems.objects.all()
    context = {'rooms': room, 'foods': foods}
    if request.method == "POST":
        room_num = request.POST['customer_room_num']
        customer_name = request.POST['customer_name']
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        customer_address = request.POST['customer_address']
        customer_checkin = request.POST['customer_checkin']
        customer_checkout = request.POST['customer_checkout']
        customer_roomprice = request.POST['customer_roomprice']
        customer_email = request.POST['customer_email']
        totalamount = request.POST['totalamount']
        emailmessage = EmailMessage(
            "Receipt From Benju Hotel",
            " Customer Name :" + customer_name + "\n"
                                                 " Customer Phone :" + customer_phone + "\n"
                                                                                        " Customer Address :" + customer_address + "\n"
                                                                                                                                   " Check In Date : " + customer_checkin + "\n"
                                                                                                                                                                            " Check Out Date : " + customer_checkout + "\n"
                                                                                                                                                                                                                       " Total Price - Rooms and Foods " + "$" + totalamount,
            "benju.web@gmail.com",
            [customer_email],
        )
        emailmessage.send()
        form = customercheckoutForm(request.POST, request.FILES)
        form.save()
        room = RoomBook.objects.get(room_num=room_num)
        room.check_out_status = True
        room.save()
        print("Room Booked")
        context['success'] = True
        context['message'] = 'Check Out Success'
        return redirect("roomstatement")
    else:
        form = RoomForm()
        FoodForm()
    return render(request, "roomstatement.html", context)


def update(request, p_id):
    context = {'success': False}
    book = RoomBook.objects.get(id=p_id)
    form = RoomForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("roomstatement")
    return render(request, "updatepage.html", {'book': book, 'form': form})


def updatepage(request):
    return render(request, "updatepage.html")
