# blog/admin.py

from django.contrib import admin
from .models import Post  # Import our Post blueprint from models.py

# This single line of code tells the admin site to manage our Post objects.
admin.site.register(Post)