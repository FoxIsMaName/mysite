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
        
   
class Income(models.Model):
    income_text = models.CharField(max_length=200)
    earning = models.FloatField(default=0)
    type_income = models.CharField(max_length=200, default='salary')
    pub_date = models.DateTimeField('date published')

    def __flo__(self):
        return self.earning 

    def __str__(self):
        return self.pub_date 

    def __str__(self):
        return self.type_income

    def __str__(self):
        return self.income_text

class Payment(models.Model):
    payment_text = models.CharField(max_length=200)
    buy_thing = models.FloatField(default=0)
    type_payment = models.CharField(max_length=200, default='food')
    pub_date = models.DateTimeField('date published')

    def __flo__(self):
        return self.buy_thing

    def __str__(self):
        return self.type_payment

    def __str__(self):
        return self.pub_date 

    def __str__(self):
        return self.payment_text

class TypeIncome(models.Model):
    type_income = models.CharField(max_length=200)
    
    def __str__(self):
        return self.type_income

class TypePayment(models.Model):
    type_payment = models.CharField(max_length=200)

    def __str__(self):
        return self.type_payment

