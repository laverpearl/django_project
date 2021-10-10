from django.shortcuts import render
from django.views.generic import ListView, DetailView
from phone.models import Phone

# Create your views here.


class PhoneLV(ListView):
    model = Phone


class PhoneDV(DetailView):
    model = Phone
