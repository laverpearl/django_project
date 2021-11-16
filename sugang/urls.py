from django.urls import path
from sugang import views

app_name = 'sugang'
urlpatterns = [
    path('', views.SugangLV.as_view(), name='index'),
    path('<int:pk>/', views.SugangDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),

    path('add/', views.SugangCreateView.as_view(), name="add"),
    path('change/', views.SugangChangeLV.as_view(), name="change"),
    path('<int:pk>/update/', views.SugangUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.SugangDeleteView.as_view(), name="delete"),
]