from django.urls import path
from . import views

# codes for creating list of posts
"""
urlpatterns = [
        path('', views.index),
      ]
"""

urlpatterns = [
        path('<int:pk>/', views.single_post_page),
        path('', views.index),
        ]
