from django.contrib import admin
from .models import Income, Payment, TypeIncome, TypePayment
# Register your models here.

admin.site.register(Income)
admin.site.register(Payment)
admin.site.register(TypeIncome)
admin.site.register(TypePayment)
