from django import forms

class searchForm(forms.Form):
    search_term = forms.CharField(label='Search')

class searchForm2(forms.Form):
    search_term = forms.CharField(label='Search')