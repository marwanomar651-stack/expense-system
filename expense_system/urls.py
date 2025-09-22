from django.contrib import admin
from django.urls import path
from main.views import dashboard, custody_list, add_custody, add_expense

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('custodies/', custody_list, name='custody_list'),
    path('custodies/add/', add_custody, name='add_custody'),
    path('expenses/add/', add_expense, name='add_expense'),
]