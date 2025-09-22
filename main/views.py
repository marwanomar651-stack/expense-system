from django.shortcuts import render
from .models import Custody, Expense

def dashboard(request):
    total_custodies = Custody.objects.count()
    total_expenses = Expense.objects.count()
    return render(request, 'dashboard.html', {
        'total_custodies': total_custodies,
        'total_expenses': total_expenses
    })

def custody_list(request):
    # دي صفحة عرض العهد - هنضيف محتواها بعدين
    return render(request, 'custody_list.html')

def add_custody(request):
    # دي صفحة إضافة عهدة - هنضيف محتواها بعدين
    return render(request, 'add_custody.html')

def add_expense(request):
    # دي صفحة إضافة مصروف - هنضيف محتواها بعدين
    return render(request, 'add_expense.html')