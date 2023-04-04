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
    class Meta:
        model = User
        fields = ('email', 'nickname', 'age', 'gender', 'skin_type', 'address')
        labels = {
            'email': '',
            'nickname': '',
            'age': '',
            'gender': '',
            'skin_type': '',
            'address': '',
        }
        widgets = {
            'email': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Email'}),
            'nickname': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nickname'}),
            'age': forms.NumberInput(attrs = {'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Gender'}),
            'skin_type': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Skin Type'}),
            'address': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Address'}),
        }