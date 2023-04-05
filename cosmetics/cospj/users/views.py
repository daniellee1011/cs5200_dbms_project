from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import User

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            messages.success(request, "Logged in successfully!")
            print("Logged successfully")
            login(request, user)
        else:
            messages.warning(request, "Invalid username or password!")
            print("Login failed")
        
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    
    return redirect("home")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        nickname = request.POST["nickname"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        skin_type = request.POST["skin_type"]
        address = request.POST["address"]
        email = request.POST["email"]
        is_superuser = request.POST["is_superuser"]
        is_staff = request.POST["is_staff"]
        
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password,
            nickname = nickname,
            age = age,
            gender = gender,
            skin_type = skin_type,
            address = address,
            is_superuser = is_superuser,
            is_staff = is_staff,
        )
        user.save()
        return redirect("user:login")
        
    return render(request, "users/signup.html")