import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    note = models.CharField(max_length=200)
    money = models.FloatField(default=0)
    type_note = models.CharField(max_length=200, default='salary')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pub_date

    def __str__(self):
        return self.type_note

    def __flo__(self):
        return self.money

    def __str__(self):
        return self.note

class TypeIncome(models.Model):
    type_income = models.CharField(max_length=200)
    
    def __str__(self):
        return self.type_income

class TypePayment(models.Model):
    type_payment = models.CharField(max_length=200)

    def __str__(self):
        return self.type_payment

