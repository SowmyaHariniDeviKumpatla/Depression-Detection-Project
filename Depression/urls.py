from django.urls import path
from . import views  # Assuming you have views.py in your app

urlpatterns = [
    # Define the home page route for the app (adjust the view name as needed)
    path('', views.home, name='home'),
    
    # Define other views you may have
    path('about/', views.about, name='about'),
]
