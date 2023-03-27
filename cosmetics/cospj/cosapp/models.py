from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ProductCategory(models.Model):
    cateName = models.CharField(max_length=50)

class ProductType(models.Model):
    cateName = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=50)

class CosmeticCompany(models.Model):
    companyName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class CosmeticBrand(models.Model):
    companyName = models.ForeignKey(CosmeticCompany, on_delete=models.CASCADE)
    brandName = models.CharField(max_length=50)
    priceRange = models.CharField(max_length=30)

class Product(models.Model):
    typeName = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    brandName = models.ForeignKey(CosmeticBrand, on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)
    avgRating = models.DecimalField(max_digits=10, decimal_places=2)
    numReviews = models.IntegerField(max_length=10)
    ingredients = models.TextField()

class Store(models.Model):
    storeName = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=30)
    products = models.ManyToManyField(Product)

class UserReview(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    ratingOption = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=ratingOption, null= True)
    description = models.TextField()