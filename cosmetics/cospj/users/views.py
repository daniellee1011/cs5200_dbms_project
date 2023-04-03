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
        
        user = User.objects.create_user(username, email, password, nickname, age, gender, skin_type, address)
        user.nickname = nickname
        user.age = age
        user.gender = gender
        user.skin_type = skin_type
        user.address = address
        user.save()
        # login(request, user) : redirect to the status already login
        return redirect("user:login")
        
    return render(request, "users/signup.html")