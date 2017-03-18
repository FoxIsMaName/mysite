from django.contrib import admin
from .models import Account, TypeIncome, TypePayment
# Register your models here.

admin.site.register(Account)
admin.site.register(TypeIncome)
admin.site.register(TypePayment)
