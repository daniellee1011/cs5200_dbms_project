"""cospj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import cosapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cosapp.views.home, name='home'),
    path('users/', include("users.urls")),
    path('review/<int:id>', cosapp.views.addReview, name='review'),
    path('deletereview/<int:product_id>/<int:userreview_id>', cosapp.views.deleteReview, name='delete_review'),
    path('editreview/<int:product_id>/<int:userreview_id>', cosapp.views.editReview, name='edit_review'),
    path('addproduct/', cosapp.views.addProduct, name='add_product'),
    path('editproduct/<int:id>', cosapp.views.editProduct, name='edit_product'),
    path('deleteproduct/<int:id>', cosapp.views.deleteProduct, name='delete_product'),
    path('productdetail/<int:id>', cosapp.views.productDetail, name = 'productdetail'),
    path('productdetail/<str:name>', cosapp.views.productdetail_name, name = 'productdetail-name'),
    path('producttype/<int:id>', cosapp.views.productType, name = 'producttype'),
    path('search_products', cosapp.views.search_products, name = "search-products"),
    path('list_types', cosapp.views.list_types, name = 'list-types'),
    path('show_type/<type_id>', cosapp.views.show_type, name = 'show-type'),
    path('update_profile/', cosapp.views.update_profile, name = 'update-profile'),
]