from django import forms


class GwamokSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
