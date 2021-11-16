from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sugang.models import Sugang

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from django.views.generic import FormView
from sugang.forms import SugangSearchForm
from django.db.models import Q

class SugangLV(ListView):
    model = Sugang


class SugangDV(DetailView):
    model = Sugang


class SearchFormView(FormView):
    form_class = SugangSearchForm
    template_name = 'sugang/sugang_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        sugang_list = Sugang.objects.filter(Q(name__icontains=searchWord) | Q(professor__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = sugang_list

        return render(self.request, self.template_name, context)  # No Redirection


class SugangCreateView(LoginRequiredMixin, CreateView):
    model = Sugang
    fields = ['gwamoknum', 'semester', 'name', 'professor', 'day', 'time', 'classroom']
    success_url = reverse_lazy('sugang:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class SugangChangeLV(LoginRequiredMixin, ListView):
    template_name = 'sugang/sugang_change_list.html'

    def get_queryset(self):
        return Sugang.objects.filter(owner=self.request.user)


class SugangUpdateView(OwnerOnlyMixin, UpdateView):
    model = Sugang
    fields = ['gwamoknum', 'semester', 'name', 'professor', 'day', 'time', 'classroom']
    success_url = reverse_lazy('sugang:index')


class SugangDeleteView(OwnerOnlyMixin, DeleteView):
    model = Sugang
    success_url = reverse_lazy('sugang:index')