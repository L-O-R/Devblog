# blog/models.py

from django.db import models
from django.contrib.auth.models import User # We need to import Django's built-in User model

# This class is our blueprint for a blog post. Django will turn this into a database table.
class Post(models.Model):
    # What information does a post need?
    
    # A title, which is a short line of text.
    title = models.CharField(max_length=200)
    
    # The main content, which is a long block of text.
    content = models.TextField()
    
    # The author. This links to a User. If a user is deleted, all their posts are also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # The date and time it was created. Django will automatically set this when we create a post.
    created_at = models.DateTimeField(auto_now_add=True)

    # A helper method to make our posts look nice in the admin panel.
    def __str__(self):
        return self.title