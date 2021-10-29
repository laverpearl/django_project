from django.urls import path
# from phone.views import PhoneLV, PhoneDV
from phone import views

app_name = 'phone'
urlpatterns = [
    path('', views.PhoneLV.as_view(), name='index'),
    path('<int:pk>/', views.PhoneDV.as_view(), name='detail'),
    path('searh/', views.SearchFormView.as_view(), name='search'),

    path('add/', views.PhoneCreateView.as_view(), name="add"),
    path('change/', views.PhoneChangeLV.as_view(), name="change"),
    path('<int:pk>/update/', views.PhoneUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.PhoneDeleteView.as_view(), name="delete"),
]