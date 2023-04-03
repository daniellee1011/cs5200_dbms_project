from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('productType', 'cosmeticBrand', 'name', 'price', 'size', 'ingredients')

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ('stars', 'description')
        
class UserProfileUpdateForm(UserChangeForm):
    email = forms.EmailField(required = True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')