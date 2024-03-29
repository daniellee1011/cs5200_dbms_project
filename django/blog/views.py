from django.shortcuts import render
from .models import Post

# Create your views here.

# codes for creating list of posts
def index(request):
    posts = Post.objects.all()

    return render(
            request,
            'blog/index.html',
            {
                'posts': posts,
                }
            )

def single_post_page(request, pk):
    post = Post.objects.get(pk = pk)

    return render(
            request,
            'blog/single_post_page.html',
            {
                'post': post,
                }
            )

def post_view(request):
    posts = Post.objects.all() # Save every object of Post table into posts variable
    return render(request, 'blog/index.html', {"posts": posts})
