from django import forms

class SugangSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
