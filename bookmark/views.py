from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from django.views.generic import FormView
from bookmark.forms import BookmarkSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark


class SearchFormView(FormView):
    form_class = BookmarkSearchForm
    template_name = 'bookmark/bookmark_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        bookmark_list = Bookmark.objects.filter(Q(id__icontains=searchWord) | Q(title__icontains=searchWord) | Q(
            url__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = bookmark_list

        return render(self.request, self.template_name, context)  # No Redirection
