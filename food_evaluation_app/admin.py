from django.contrib import admin
from .models import Appointment, Dish, Restaurant, Review

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'dish', 'user', 'date')

admin.site.register(Dish, DishAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Restaurant)
admin.site.register(Appointment)