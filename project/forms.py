from django import forms
from project.models import Staff, Food, OrderedItems, RoomBook, customercheckout, OrderedFoodItems


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class OrderedFoodItemsForm(forms.ModelForm):
    class Meta:
        model = OrderedFoodItems
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderedItems
        fields = "__all__"


class RoomForm(forms.ModelForm):
    class Meta:
        model = RoomBook
        fields = "__all__"


class customercheckoutForm(forms.ModelForm):
    class Meta:
        model = customercheckout
        fields = "__all__"


