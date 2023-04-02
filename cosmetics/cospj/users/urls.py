from django.urls import path
from . import views 

app_name = "user"

urlpatterns = [
    path("login", views.login_view, name = "login"),
    path("logout", views.logout_view, name = "logout"),
    path("signup", views.signup_view, name = "signup"),
    path("search_venues", views.search_venues, name = "search_venues")
]