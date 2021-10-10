from django.urls import path
from phone.views import PhoneLV, PhoneDV

app_name = 'phone'
urlpatterns = [
    path('', PhoneLV.as_view(), name='index'),
    path('<int:pk>/', PhoneDV.as_view(), name='phonedetail'),
]