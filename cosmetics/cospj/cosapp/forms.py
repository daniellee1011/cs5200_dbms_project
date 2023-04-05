from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('productType', 'cosmeticBrand', 'name', 'price', 'size', 'ingredients')

    stores = forms.ModelMultipleChoiceField(queryset=Store.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)       

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
                        
            initial = kwargs.setdefault('initial', {})
            initial['stores'] = [t.pk for t in kwargs['instance'].store_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
       
        instance = forms.ModelForm.save(self, False)

        old_save_m2m = self.save_m2m
        def save_m2m():
           old_save_m2m()
           
           instance.store_set.clear()
           instance.store_set.add(*self.cleaned_data['stores'])
        self.save_m2m = save_m2m

        if commit:
            instance.save()
            self.save_m2m()

        return instance

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