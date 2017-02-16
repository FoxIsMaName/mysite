from django.db import models

# Create your models here.
class Income(models.Model):
    income_text = models.CharField(max_length=200)
    earning = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.income_text

    def __int__(self):
        return self.earning 

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Payment(models.Model):
    payment_text = models.CharField(max_length=200)
    buy_thing = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.payment_text

    def __int__(self):
        return self.buy_thing

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class IncomeType(models.Model):
    income_list = models.ForeignKey(Income, on_delete=models.CASCADE)
    income_type = models.CharField(max_length=200)

    def __str__(self):
        return self.income_type

class PaymentType(models.Model):
    payment_list = models.ForeignKey(Payment, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=200)

    def __str__(self):
        return self.payment_type


