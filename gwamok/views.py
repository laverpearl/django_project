from django.shortcuts import render
from django.views.generic import ListView, DetailView
from gwamok.models import Gwamok

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from django.views.generic import FormView
from gwamok.forms import GwamokSearchForm
from django.db.models import Q



class GwamokLV(ListView):
    model = Gwamok


class GwamokDV(DetailView):
    model = Gwamok


class SearchFormView(FormView):
    form_class = GwamokSearchForm
    template_name = 'gwamok/gwamok_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        student_list = Gwamok.objects.filter(Q(name__icontains=searchWord) | Q(professor__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = gwamok_list # 여기 수정

        return render(self.request, self.template_name, context)  # No Redirection


class GwamokCreateView(LoginRequiredMixin, CreateView):
    model = Gwamok
    fields = ['gwamoknum', 'semester', 'name', 'professor', 'day', 'time', 'classroom', 'limitnum']
    success_url = reverse_lazy('gwamok:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class GwamokChangeLV(LoginRequiredMixin, ListView):
    template_name = 'gwamok/gwamok_change_list.html'

    def get_queryset(self):
        return Gwamok.objects.filter(owner=self.request.user)


class GwamokUpdateView(OwnerOnlyMixin, UpdateView):
    model = Gwamok
    fields = ['gwamoknum', 'semester', 'name', 'professor', 'day', 'time', 'classroom', 'limitnum']
    success_url = reverse_lazy('gwamok:index')


class GwamokDeleteView(OwnerOnlyMixin, DeleteView):
    model = Gwamok
    success_url = reverse_lazy('gwamok:index')