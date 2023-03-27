from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    
    return render(request, 'home.html')


def addReview(request, id):
    post = Product.objects.get(id = id)
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(id=1)
                stars = request.POST.get('stars')
                description = request.POST.get('description')
                review = UserReview(product=post, user=user, stars=stars, description=description)
                review.save()
                return redirect('home')
            except:
                pass

    form = UserReviewForm()

    return render(request, 'addreview.html', {'form':form})

def addProduct(request):
    form = ProductForm()
    
    context = {
        "form":form
    }
    template_name = 'addproduct.html'
    return render(request, template_name, context)


