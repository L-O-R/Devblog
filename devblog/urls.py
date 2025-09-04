    # devblog/urls.py
from django.contrib import admin
from django.urls import path, include # Make sure to import "include"
    
urlpatterns = [
    path('admin/', admin.site.urls),
    # This line tells Django: for any URL that isn't 'admin/',
    # go look for more instructions in the 'urls.py' file inside the 'blog' app.
    path('', include('blog.urls')),
]