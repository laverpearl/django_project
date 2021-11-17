from django import forms
# from django.forms import inlineformset_factory
# from sugang.models import Sugang, Gwamok

# SugangInlineFormSet = inlineformset_factory(Sugang, Gwamok, fields=['gwamok'], extra=2)
class SugangSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
