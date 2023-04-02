from django.db import models
from users.models import User
from django.utils import timezone

class ProductCategory(models.Model):
    cateName = models.CharField(max_length=50)

    def __str__(self):
        return self.cateName

class ProductType(models.Model):
    productCategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=50)

    def __str__(self):
        return self.typeName

class CosmeticCompany(models.Model):
    companyName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.companyName

class CosmeticBrand(models.Model):
    cosmeticCompany = models.ForeignKey(CosmeticCompany, on_delete=models.CASCADE)
    brandName = models.CharField(max_length=50)
    priceRange = models.CharField(max_length=30)

    def __str__(self):
        return self.brandName

class Product(models.Model):
    productType = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    cosmeticBrand = models.ForeignKey(CosmeticBrand, on_delete=models.CASCADE)
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