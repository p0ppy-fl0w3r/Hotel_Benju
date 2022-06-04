from django.contrib import admin
from django.urls import path, include
from . import views

# Django admin customization
urlpatterns = [


    path('', views.home, name='home'),  # signin as well
    path('signup', views.signup, name='signup'),  # signup is creating a Customer as well
    path('MainHome', views.MainHome, name='MainHome'),
    path('food', views.food, name='food'),
    path('signout', views.signout, name='sign-out'),
    path('menu', views.menu, name='menu'),
    path('updatepage', views.updatepage, name='updatepage'),
    path('show/', views.show, name='show'),
    path('showbookedrooms/<str:search_param>', views.showbookedrooms, name='showbookedrooms'),
    path('foodorders', views.foodorders, name='foodorders'),
    path('showmenu', views.showmenu, name='showmenu'),
    path('showstaffs', views.showstaffs, name='showstaffs'),
    path('roomstatement', views.roomstatement, name='roomstatement'),
    path('update/<str:p_id>', views.update, name="update"),
    # path('StatementforAdmin', views.StatementforAdmin, name="StatementforAdmin"),

    # path('admin', views.admin, name='admin'),
    path('room_booked', views.room_booked, name='room_booked'),
    path('delete_staff/<int:P_id>', views.delete_staff, name="delete_staff"),
    path('delete_foodadmin/<int:P_id>', views.delete_foodadmin, name="delete_foodadmin"),
    path('OrderServed/<int:P_id>', views.OrderServed, name="OrderServed"),
    path('delete_book/<int:P_id>', views.delete_book, name="delete_book"),
    path('delete_roombook/<int:P_id>', views.delete_roombook, name="delete_roombook"),
    path('checkout/<int:P_id>', views.checkout, name="checkout"),
    path('delete_item/<int:P_id>', views.delete_item, name="delete_item"),
    path('search', views.search, name="search"),

    path('searchitem', views.searchitem, name="searchitem"),

    path('ordered', views.ordered, name="ordered"),
    path('add', views.add, name="add"),
    path('create_items', views.create_items, name='create_items'),
    path('create', views.create, name='create'),
    path('create', views.create, name='create'),
    path('orderconfirm', views.orderconfirm, name='orderconfirm'),



    # path('room', views.room, name='room'),
    # path('delete_costumer/<int:P_id>', views.delete_customer, name="delete_customer"),
    # path('search', views.search, name="search"),
    # path('searchproduct', views.searchproduct, name="searchproduct"),
    # path('Page_next/', views.Page_next, name="Page_next"),

]
