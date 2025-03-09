from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The admin page for your Django app
    path('admin/', admin.site.urls),
    
    # Include URLs from your app (replace 'Depression' with your actual app name)
    path('depression/', include('Depression.urls')),
]
