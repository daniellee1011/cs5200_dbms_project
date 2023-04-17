from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connections
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
                print('addReview: call MySQL add_review procedure')
                connection = connections['default']
                with connection.cursor() as cursor:
                    cursor.callproc('add_review',[
                        product.id,
                        current_user.id,
                        form.cleaned_data['stars'],
                        form.cleaned_data['description']
                    ])

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

def check_superuser(username):
    print('check_superuser: call MySQL check_superuser function')
    connection = connections['default']
    with connection.cursor() as cursor:
        cursor.execute('SELECT check_superuser(%s)', [username])
        is_superuser = cursor.fetchone()[0]
    return is_superuser

def addProduct(request):
    if request.user.is_authenticated:
        if check_superuser(request.user.username):
            if request.method == 'POST':
                form = ProductForm(request.POST)

                if form.is_valid():
                    print('addProduct: call MySQL insert_product procedure')
                    connection = connections['default']
                    with connection.cursor() as cursor:
                        cursor.callproc('insert_product',[
                            form.cleaned_data['productType'],
                            form.cleaned_data['cosmeticBrand'],
                            form.cleaned_data['name'],
                            form.cleaned_data['price'],
                            form.cleaned_data['size'],
                            0, # avgRating has default value of 0, so don't need to inclue it in the form data
                            0,
                            form.cleaned_data['ingredients']
                        ])
                    messages.success(request, "Product added.")
                    return redirect('home')

            form = ProductForm()

            return render(request, 'addproduct.html', {'form':form})

def editProduct(request, id):
    if request.user.is_authenticated:
        if check_superuser(request.user.username):
            product = Product.objects.get(id = id)
            if request.method == 'POST':
                            
                form = ProductForm(request.POST, instance=product)
                messages.error(request, form.errors)
                if form.is_valid():
                    print('editProduct: call MySQL edit_product procedure')
                    connection = connections['default']
                    with connection.cursor() as cursor:
                        cursor.callproc('edit_product',[
                            product.id,
                            form.cleaned_data['productType'],
                            form.cleaned_data['cosmeticBrand'],
                            form.cleaned_data['name'],
                            form.cleaned_data['price'],
                            form.cleaned_data['size'],
                            form.cleaned_data['ingredients']
                        ])
                    messages.success(request, "Product edited.")
                    return redirect('productdetail', id)
                            
                else:
                    return redirect('home')
        
            form = ProductForm(instance=product)

            return render(request, 'addproduct.html', {'form':form})
        
    return redirect('home')
    
def deleteProduct(request, id):
    if request.user.is_authenticated:
        if check_superuser(request.user.username):
            product = Product.objects.get(id = id)
            print('deleteProduct: call MySQL delete_product procedure')
            connection = connections['default']
            with connection.cursor() as cursor:
                cursor.callproc('delete_product', [product.id])
            messages.success(request, "Product deleted.")
            return redirect('home')
    
    return redirect('home')
    
def productDetail(request, id):
    product = Product.objects.get(id=id)
    store = Store.objects.filter(products=product.id)
    stores = ', '.join(str(x) for x in store)
    reviews = UserReview.objects.filter(product_id = id)

    return render(request, "productdetail.html", context = {"product":product, "reviews":reviews, "store":stores})

def productType(request, id):
    products = Product.objects.filter(productType_id = id)

    return render(request, "productlist.html", context = {"productlist":products})

def productdetail_name(request, name):
    product = Product.objects.get(name=name)
    return render(request, 'productdetail.html', {'product': product})
    
def search_products(request):
    if request.method == "POST":
        searched = request.POST.get('searched')

        connection = connections['default']
        with connection.cursor() as cursor:
            cursor.callproc('search_product_by_name', [searched])
            products = cursor.fetchall()

        return render(request, "events/search_products.html", {'searched': searched, 'products': products})
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
            print('update_profile: call update_profile procedure')
            username = request.user.username
            connection = connections['default']
            with connection.cursor() as cursor:
                cursor.callproc('update_profile', [username, form.cleaned_data['email'], form.cleaned_data['nickname'], form.cleaned_data['age'], form.cleaned_data['gender'], form.cleaned_data['skin_type'], form.cleaned_data['address']])
            return redirect('update-profile')
    else:
        form = UserProfileUpdateForm(instance = request.user)

    print('update_profile: call search_review_by_user procedure')
    user_id = request.user.id
    connection = connections['default']
    with connection.cursor() as cursor:
        cursor.callproc('search_review_by_user', [user_id])
        reviews = cursor.fetchall()
        
    return render(request, 'events/update_profile.html', context = {'form': form, 'reviews': reviews})