from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('custodies/', views.custody_list, name='custody_list'),
    path('custodies/add/', views.add_custody, name='add_custody'),
    path('expenses/add/', views.add_expense, name='add_expense'),
]