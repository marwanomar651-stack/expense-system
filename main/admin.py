from django.contrib import admin
from .models import Custody, Expense

class CustodyAdmin(admin.ModelAdmin):
    list_display = ['employee', 'amount', 'status', 'start_date']
    list_filter = ['status', 'start_date']

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['employee', 'amount', 'type', 'date']
    list_filter = ['type', 'date']

admin.site.register(Custody, CustodyAdmin)
admin.site.register(Expense, ExpenseAdmin)