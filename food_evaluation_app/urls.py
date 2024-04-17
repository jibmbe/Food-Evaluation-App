from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('add_review/', views.add_review, name='add_review'),
    path('restaurant/<int:restaurant_id>/about/', views.about, name='about'),
]
