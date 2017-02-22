from django.shortcuts import render
from django.utils import timezone
from .models import Income, Payment, TypeIncome, TypePayment
# Create your views here.

def callMainPage(request): 
    income_list = Income.objects.order_by('-pub_date')[:5]
    payment_list = Payment.objects.order_by('-pub_date')[:5]

    #calulation the rest of money
    income_sum = 0
    payment_sum = 0

    for income in income_list :
        income_sum += income.earning
    for payment in payment_list :
        payment_sum += payment.buy_thing

    remain_money = income_sum - payment_sum
    return render(request, 'ManMon/main.html',{'remain_money':remain_money,         
                  'income_list':income_list, 'payment_list':payment_list})

#show payment information
def tableIncome(request):
    income_list = Income.objects.order_by('-pub_date')
    income_sum = 0
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

def callInsertIncome(request):
    type_in_list = TypeIncome.objects.order_by('-type_income')
    return render(request,"ManMon/insertIncome.html", {'type_in_list':type_in_list})

#save income information
def saveIncome(request):
    income_list = Income.objects.order_by('-pub_date')
    income_sum = 0
    for income in income_list :
        income_sum += income.earning

    try:
        note_income = request.POST['note_income']
        money = request.POST['money']
        date_income = request.POST['dmy_income']
        type_income = request.POST['type_income']
    except:
        note_income = ""
        money = ""
        date_income = ""
        type_income = ""
    else:
            IN = Income(income_text=note_income, earning=money, type_income = type_income, pub_date=date_income)
            IN.save()

    return render(request,"ManMon/showIncome.html",{'income_list':income_list,'incomesum':income_sum})

def callInsertPayment(request):
    type_pay_list = TypePayment.objects.order_by('-type_payment')    
    return render(request, "ManMon/insertPayment.html",{"type_pay_list":type_pay_list})

#save income information
def savePayment(request):
    payment_list = Payment.objects.order_by('-pub_date')
    payment_sum = 0
    for payment in payment_list :
        payment_sum += payment.buy_thing

    try:
        note_payment = request.POST['note_payment']
        payment = request.POST['payment']
        date_payment = request.POST['dmy_payment']
        type_payment = request.POST['type_payment']
    except:
        note_payment = ""
        payment = ""
        date_payment = ""
        type_payment = ""
    else:
            OUT = Payment(payment_text=note_payment, buy_thing=payment, type_payment = type_payment, pub_date=date_payment)
            OUT.save()

    return render(request,"ManMon/showPayment.html",{'payment_list':payment_list, 'paymentsum':payment_sum})


