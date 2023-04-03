from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def addReview(request, id):
    product = Product.objects.get(id = id)
    print(product)
    current_user = request.user
    print(current_user)
    if request.user.is_authenticated:

        if request.method == 'POST':

            form = UserReviewForm(request.POST)

            if form.is_valid():
                
                if UserReview.objects.filter(user_id=current_user.id, product_id = product.id).exists():
                    return redirect('productdetail', id)
               
                stars = request.POST.get('stars')
                description = request.POST.get('description')
                review = UserReview(product_id=product.id, user_id=current_user.id, stars=stars, description=description)
                review.save()

                return redirect('productdetail', id)

                
    else:
        return redirect('home')

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
    reviews = UserReview.objects.filter(product_id = id)

    return render(request, "productdetail.html", context = {"product":product, "reviews":reviews})

def productType(request, id):
    products = Product.objects.filter(productType_id = id)

    return render(request, "productlist.html", context = {"productlist":products})

def productdetail_name(request, name):
    product = Product.objects.get(name=name)
    return render(request, 'productdetail.html', {'product': product})
    
def search_products(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        products = Product.objects.filter(name__contains = searched)
        return render(request, "events/search_products.html", {'searched' : searched, 'products': products})
    else:
        return render(request, "events/search_products.html")

def show_type(request, id):
    type = ProductType.objects.get(pk=id)
    return render(request, 'events/show_type.html', {'type': type})

def list_types(request):
    type_list = ProductType.objects.all()
    return render(request, 'events/type.html', {'type_list': type_list})