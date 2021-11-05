from django.shortcuts import render
from django.views.generic import ListView, DetailView
from namecard.models import Namecard

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

from django.views.generic import FormView
from namecard.forms import NamecardSearchForm
from django.db.models import Q

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


# 아랫줄부터 추가 -----------------------------------------------
class NamecardCreateView(LoginRequiredMixin, CreateView):
    model = Namecard
    fields = ['name', 'tel', 'company', 'email', 'group']
    success_url = reverse_lazy('namecard:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NamecardChangeLV(LoginRequiredMixin, ListView):
    template_name = 'namecard/namecard_change_list.html'

    def get_queryset(self):
        return Namecard.objects.filter(owner=self.request.user)


class NamecardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Namecard
    fields = ['name', 'tel', 'company', 'email', 'group']
    success_url = reverse_lazy('namecard:index')


class NamecardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Namecard
    success_url = reverse_lazy('namecard:index')