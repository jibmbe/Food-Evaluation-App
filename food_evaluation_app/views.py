from django.shortcuts import render
from .models import Restaurant, Dish, Review
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse



def home(request):
    return render(request, 'home.html')


def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

def add_review(request):
    
    return HttpResponse("Review added successfully")

def about(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'about.html', {'restaurant': restaurant})