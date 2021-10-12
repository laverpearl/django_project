from django.urls import path
from student.views import StudentLV, StudentDV

from student import views

app_name = 'student'
urlpatterns = [
    path('', StudentLV.as_view(), name='index'),
    path('<int:pk>/', StudentDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]