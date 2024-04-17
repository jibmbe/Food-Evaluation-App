from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = [(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')]
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} Star Review for {self.dish.name} by {self.user.username}"
    
class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    number_of_guests = models.IntegerField()  
    special_requests = models.TextField()     
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment at {self.restaurant} on {self.date} at {self.time}"