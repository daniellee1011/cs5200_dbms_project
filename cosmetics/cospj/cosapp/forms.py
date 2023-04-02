from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('productType', 'cosmeticBrand', 'name', 'price', 'size', 'ingredients')

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ('stars', 'description')