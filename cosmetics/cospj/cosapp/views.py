from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def addReview(request, id):
    product = Product.objects.get(id = id)

    current_user = request.user

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
                messages.success(request, "Review added.")
                return redirect('productdetail', id)

    else:
        return redirect('home')

    form = UserReviewForm()

    return render(request, 'addreview.html', {'form':form})

def deleteReview(request, product_id, userreview_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id = product_id)
        review = UserReview.objects.get(product = product, id = userreview_id)
        if request.user == review.user:
            review.delete()
            messages.success(request, "Review deleted.")
        return redirect('productdetail', product_id)
    else:
        return redirect('home')
    
def editReview(request, product_id, userreview_id):

    if request.user.is_authenticated:
        product = Product.objects.get(id = product_id)
        review = UserReview.objects.get(product = product, id = userreview_id)
        if request.user == review.user:
            if request.method == 'POST':
                
                form = UserReviewForm(request.POST, instance=review)
               
                if form.is_valid():
                  
                    form.save()
                    messages.success(request, "Review edited.")
                    return redirect('productdetail', product_id)
                            
                else:
                    return redirect('home')
           
            form = UserReviewForm(instance=review)

            return render(request, 'addreview.html', {'form':form})

def addProduct(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
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
                        messages.success(request, "Product added.")
                        return redirect('home')
                    except:
                        pass

            form = ProductForm()
    
            return render(request, 'addproduct.html', {'form':form})

def editProduct(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            product = Product.objects.get(id = id)
            if request.method == 'POST':
                            
                form = ProductForm(request.POST, instance=product)
            
                if form.is_valid():
                
                    form.save()
                    messages.success(request, "Product edited.")
                    return redirect('productdetail', id)
                            
                else:
                    return redirect('home')
        
            form = ProductForm(instance=product)

            return render(request, 'addproduct.html', {'form':form})
        
    return redirect('home')
    
def deleteProduct(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            product = Product.objects.get(id = id)

            product.delete()
            messages.success(request, "Product deleted.")
            return redirect('home')
    
    return redirect('home')
    
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
        products = Product.objects.filter(name__icontains = searched)
        return render(request, "events/search_products.html", {'searched' : searched, 'products': products})
    else:
        return render(request, "events/search_products.html")

def show_type(request, id):
    type = ProductType.objects.get(pk=id)
    return render(request, 'events/show_type.html', {'type': type})

def list_types(request):
    type_list = ProductType.objects.all()
    return render(request, 'events/type.html', {'type_list': type_list})

def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, instance = request.user)
        
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance = request.user)
        
    reviews = UserReview.objects.filter(user=request.user)
        
    return render(request, 'events/update_profile.html', context = {'form': form, 'reviews': reviews})