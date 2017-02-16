from django.shortcuts import render
from django.utils import timezone
from .models import Income, Payment
# Create your views here.

def callMainPage(request): 
    #calulation the rest of money
    income_sum = 0
    payment_sum = 0
    income_list = Income.objects.order_by('-pub_date')
    payment_list = Payment.objects.order_by('-pub_date')

    for income in income_list :
        income_sum += income.earning
    for payment in payment_list :
        payment_sum += payment.buy_thing

    remain_money = income_sum - payment_sum
    return render(request, 'ManMon/main_page.html',{'remain_money':remain_money})

#show payment information
def tableIncome(request):
    income_list = Income.objects.order_by('-pub_date')
    income_sum = 0
    print(income_list)
    for income in income_list :
        income_sum += income.earning
    return render(request, 'ManMon/showIncome.html', {'income_list':income_list,'incomesum':income_sum})

#show payment information
def tablePayment(request):
    payment_list = Payment.objects.order_by('-pub_date')
    payment_sum = 0
    for payment in payment_list :
        payment_sum += payment.buy_thing
    return render(request, 'ManMon/showPayment.html', {'payment_list':payment_list, 'paymentsum':payment_sum})

#save income information
def saveIncome(request):
    try:
        note_income = request.POST['note_income']
        money = request.POST['money']
        date_income = request.POST['dmy_income']
    except:
        note_income = ""
        money = ""
        date_income = ""
    else:
            IN = Income(income_text=note_income, earning=money, pub_date=date_income)
            IN.save()

    #calulation the rest of money
    income_sum = 0
    payment_sum = 0
    income_list = Income.objects.order_by('-pub_date')
    payment_list = Payment.objects.order_by('-pub_date')

    for income in income_list :
        income_sum += income.earning
    for payment in payment_list :
        payment_sum += payment.buy_thing

    remain_money = income_sum - payment_sum
    print(note_income)
    return render(request,"ManMon/main_page.html",{'remain_money':remain_money})

#save income information
def savePayment(request):
    try:
        note_payment = request.POST['note_payment']
        payment = request.POST['payment']
        date_payment = request.POST['dmy_payment']
    except:
        note_payment = ""
        payment = ""
        date_payment = ""
    else:
            OUT = Payment(payment_text=note_payment, buy_thing=payment, pub_date=date_payment)
            OUT.save()

    #calulation the rest of money
    income_sum = 0
    payment_sum = 0
    income_list = Income.objects.order_by('-pub_date')
    payment_list = Payment.objects.order_by('-pub_date')

    for income in income_list :
        income_sum += income.earning
    for payment in payment_list :
        payment_sum += payment.buy_thing

    remain_money = income_sum - payment_sum
    return render(request,"ManMon/main_page.html",{'remain_money':remain_money})
