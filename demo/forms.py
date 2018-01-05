# -*- coding: utf-8 -*-
from django import forms
from .models import CategoryModel,PhoneBrand,PhoneModel

class CategoryForm(forms.ModelForm):
    id=forms.CharField(max_length=50,widget=forms.HiddenInput())
    is_favorite=forms.TypedChoiceField(label='Favorites',choices=((False, 'False'), (True, 'True')),widget=forms.RadioSelect())

    class Meta:
        model=CategoryModel
        fields=(
            'id',
            'is_favorite',
        )

class BrandForm(forms.ModelForm):
    id=forms.CharField(max_length=50,widget=forms.HiddenInput())
    is_favorite=forms.TypedChoiceField(label='Favorites',choices=((False, 'False'), (True, 'True')),widget=forms.RadioSelect())

    class Meta:
        model=PhoneBrand
        fields=(
            'id',
            'is_favorite',
        )

class PhoneForm(forms.ModelForm):
    id=forms.CharField(max_length=50,widget=forms.HiddenInput())
    is_active=forms.TypedChoiceField(label='Active',choices=((False, 'False'), (True, 'True')),widget=forms.RadioSelect())

    class Meta:
        model=PhoneModel
        fields=(
            'id',
            'is_active',
        )