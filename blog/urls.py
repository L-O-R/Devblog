    # blog/urls.py
from django.urls import path
from . import views
    
urlpatterns = [
        # This is our existing homepage URL
    path('', views.post_list, name='post_list'),
    
        # ADD THIS NEW DYNAMIC URL PATTERN
        # The <int:pk> part is a converter that captures an integer from the URL
        # and passes it as a keyword argument named 'pk' to our view.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('post-list-api', views.post_list_api, name="post-list-api"),
    path('post-detail-api/<int:pk>', views.post_detail_api, name="post-detail-api"),
]