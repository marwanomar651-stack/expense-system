from django.db import models
from django.contrib.auth.models import User

class Custody(models.Model):
    STATUS_CHOICES = [
        ('new', 'عهدة جديدة'),
        ('in_progress', 'قيد التسوية'),
        ('closed', 'مسددة')
    ]
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    start_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employee.username} - {self.amount}"

class Expense(models.Model):
    TYPE_CHOICES = [
        ('transport', 'مواصلات'),
        ('supplies', 'مستلزمات مكتبية'),
        ('maintenance', 'صيانة'),
        ('other', 'أخرى')
    ]
    
    custody = models.ForeignKey(Custody, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.username} - {self.amount} - {self.type}"