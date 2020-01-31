from django.contrib import admin

# Register your models here.
from pizzas.models import Pizza
from pizzas.models import Topping

admin.site.register(Pizza)
admin.site.register(Topping)
