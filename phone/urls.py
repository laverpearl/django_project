from django.urls import path
from phone.views import PhoneLV, PhoneDV

from phone import views

app_name = 'phone'
urlpatterns = [
    path('', PhoneLV.as_view(), name='index'),
    path('<int:pk>/', PhoneDV.as_view(), name='detail'),
    path('searh/', views.SearchFormView.as_view(), name='search'),
]