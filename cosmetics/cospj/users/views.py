from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            print("logged successfully")
            login(request, user)
        else:
            print("login failed")
        
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    
    return redirect("user:login")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        user_id = request.POST["user_id"]
        
        user = User.objects.create_user(username, email, password)
        user.lastname = lastname
        user.firstname = firstname
        user.user_id = user_id
        user.save()
        # login(request, user) : redirect to the status already login
        return redirect("user:login")
        
    return render(request, "users/signup.html")

# https://www.youtube.com/watch?v=AGtae4L5BbI
def search_venues(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        return render(request, "search_venues.html", {"searched" : searched})
    else:
        return render(request, "search_venues.html")