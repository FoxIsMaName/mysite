from django.contrib import admin
from .models import Account, Payment, TypeIncome, TypePayment
# Register your models here.

admin.site.register(Account)
admin.site.register(Payment)
admin.site.register(TypeIncome)
admin.site.register(TypePayment)
