from django.urls import path
from namecard.views import NamecardLV, NamecardDV

from namecard import views

app_name = 'namecard'
urlpatterns = [
    path('', NamecardLV.as_view(), name='index'),
    path('<int:pk>/', NamecardDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),

]