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

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                typename = request.POST.get('productType')
                brandname = request.POST.get('cosmeticBrand')
                name = request.POST.get('name')
                price = request.POST.get('price')
                size = request.POST.get('size')
                ingredients = request.POST.get('ingredients')
                product = Product(productType_id = typename, cosmeticBrand_id = brandname, name = name, price = price, size = size, avgRating = 0, numReviews = 0, ingredients = ingredients)
                product.save()
                return redirect('home')
            except:
                pass

    form = ProductForm()
    
    return render(request, 'addproduct.html', {'form':form})

def productDetail(request, id):
    product = Product.objects.get(id=id)
    reviews = UserReview.objects.filter(product = id)

    return render(request, "productdetail.html", context = {"product":product, "reviews":reviews})
    

