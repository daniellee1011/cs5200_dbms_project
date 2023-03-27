from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('typeName', 'brandName', 'name', 'price', 'size', 'ingredients')

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ('stars', 'description')