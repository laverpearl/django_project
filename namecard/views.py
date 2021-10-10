from django.shortcuts import render
from django.views.generic import ListView, DetailView
from namecard.models import Namecard

from django.views.generic import FormView
from namecard.forms import NamecardSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.


class NamecardLV(ListView):
    model = Namecard


class NamecardDV(DetailView):
    model = Namecard


class SearchFormView(FormView):
    form_class = NamecardSearchForm
    template_name = 'namecard/namecard_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        namecard_list = Namecard.objects.filter(Q(name__icontains=searchWord) | Q(tel__icontains=searchWord) | Q(
            group__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = namecard_list

        return render(self.request, self.template_name, context)  # No Redirection
