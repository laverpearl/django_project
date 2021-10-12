from django.shortcuts import render
from django.views.generic import ListView, DetailView
from phone.models import Phone

from django.views.generic import FormView
from phone.forms import PhoneSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.


class PhoneLV(ListView):
    model = Phone


class PhoneDV(DetailView):
    model = Phone


class SearchFormView(FormView):
    form_class = PhoneSearchForm
    template_name = 'phone/phone_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        phone_list = Phone.objects.filter(Q(name__icontains=searchWord) | Q(phonenum__icontains=searchWord) | Q(
            id__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = phone_list

        return render(self.request, self.template_name, context)  # No Redirection

