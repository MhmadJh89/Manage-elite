from django import forms
from .models import Device,Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets ={
           'name' : forms.TextInput(attrs = {'class':'form-control'})
        }

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields =[
            'title',
            'company',
            'photo_device',
            'photo_company',
            'price',
            'rental_money',
            'type_device',
            'rental_price_hour', 
            'rental_period',
            'total_rental',
            'status',
            'category'
        ]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'photo_device':forms.FileInput(attrs={'class':'form-control'}),
            'photo_company':forms.FileInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_money':forms.NumberInput(attrs={'class':'form-control'}),
            'type_device':forms.Select(attrs={'class':'form-control'}),
            'rental_price_hour':forms.NumberInput(attrs={'class':'form-control', 'id':'rentalhours'}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control', 'id':'rentalprice'}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control', 'id':'totalrental'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }