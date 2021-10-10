from django.shortcuts import render
from django.views.generic import ListView, DetailView
from namecard.models import Namecard

# Create your views here.


class NamecardLV(ListView):
    model = Namecard


class NamecardDV(DetailView):
    model = Namecard
