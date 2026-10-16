from django import forms 
from products.models import Products
class ProductField(forms.ModelForm):
    class Meta:
        model = Products
        # fields = '__all__'
        exclude = ['is_available']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'



