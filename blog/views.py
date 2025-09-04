# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect # Add get_object_or_404
from .models import Post
from .forms import ContactForm 
from django.http import JsonResponse
    
    # This is our existing post_list view
def post_list(request):
    all_posts = Post.objects.all()
    context = {'all_the_posts': all_posts}
    return render(request, 'blog/index.html', context)
    
    # ADD THIS NEW VIEW
    # It takes the request and the 'pk' from the URL as arguments
def post_detail(request, pk):
        # 1. Get the single post from the Kitchen (Model)
        # Use the get_object_or_404 shortcut to get the Post.
        # If a post with the given pk doesn't exist, it will show a 404 page.
    post = get_object_or_404(Post, pk=pk)
    
        # 2. Prepare the context
    context = {
        'post': post
    }
    
    # 3. Render the final dish using a new template
    return render(request, 'blog/post_detail.html', context)



def contact(request):
        # Check if the request method is POST (i.e., the form has been submitted)
    if request.method == 'POST':
            # Create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
            # Check if the form's data is valid
        if form.is_valid():
                # Process the data in form.cleaned_data
                # For now, we'll just print it to the terminal where the server is running
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print("CONTACT FORM SUBMISSION:")
            print(f"Name: {name}, Email: {email}, Message: {message}")
    
            # Redirect to a new URL after successful submission
            return redirect('contact_success')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    
    return render(request, 'blog/contact.html', {'form': form})
    
    # ADD A VIEW FOR THE SUCCESS PAGE
def contact_success(request):
    return render(request, 'blog/contact_success.html')



#  api function

def post_list_api(request):
    all_posts = Post.objects.all()
    context = {'all_the_posts': all_posts}
    data = {
        "posts": 
            list(all_posts.values(
                'pk', 
                'title', 
                'content', 
                'author__username', 
                'created_at'))
    }
    return JsonResponse(data)