from django.urls import path
from gwamok import views

app_name = 'gwamok'
urlpatterns = [
    path('', views.GwamokLV.as_view(), name='index'),
    path('<int:pk>/', views.GwamokDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),

    path('add/', views.GwamokCreateView.as_view(), name="add"),
    path('change/', views.GwamokChangeLV.as_view(), name="change"),
    path('<int:pk>/update/', views.GwamokUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.GwamokDeleteView.as_view(), name="delete"),
]