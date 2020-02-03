from django import forms

class NameForm(forms.Form):
    id = forms.CharField(label='Product ID', max_length=100)
    name = forms.CharField(label='Product Name', max_length=100)
    price = forms.CharField(label='Price', max_length=100)

class SearchForm(forms.Form):
    name = forms.CharField(label='Product Name', max_length=100)

class ButtonForm(forms.Form):
    id=forms.CharField(label='Remove Product', max_length=100)
    
