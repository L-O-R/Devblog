# blog/forms.py
from django import forms
    
# This is our Form blueprint. It does NOT talk to the database.
# It just defines the fields for a form.
class ContactForm(forms.Form):
    # A simple text input for the user's name. It's required.
    name = forms.CharField(max_length=100)
    
    # An EmailField automatically checks if the input is a valid email address.
    email = forms.EmailField(required=True )
    
    # A CharField with a widget to make it a larger text area box.
    message = forms.CharField(widget=forms.Textarea)