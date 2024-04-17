from django.shortcuts import redirect, render
from food_evaluation_app.forms import AppointmentForm
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

def schedule_appointment(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.restaurant = restaurant
            appointment.user = request.user 
            appointment.save()
            return redirect('confirmation')  
    else:
        form = AppointmentForm()
    return render(request, 'schedule_appointment.html', {'form': form, 'restaurant': restaurant})

def confirmation(request):
    
    return render(request, 'confirmation.html')