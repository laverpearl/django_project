from django.shortcuts import render
from django.views.generic import ListView, DetailView
from student.models import Student

from django.views.generic import FormView
from student.forms import StudentSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.


class StudentLV(ListView):
    model = Student


class StudentDV(DetailView):
    model = Student


class SearchFormView(FormView):
    form_class = StudentSearchForm
    template_name = 'student/student_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        student_list = Student.objects.filter(Q(name__icontains=searchWord) | Q(tel__icontains=searchWord) | Q(
            studentnum__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = student_list

        return render(self.request, self.template_name, context)  # No Redirection


