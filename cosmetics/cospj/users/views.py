from django.shortcuts import render
from django.contrib.auth import authenticate, login

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