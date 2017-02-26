from django.shortcuts import render
from django.utils import timezone
from .models import Income, Payment, TypeIncome, TypePayment
from .models import Account

# Create your views here.

def callMainPage(request): 
    income_list = Income.objects.order_by('-pub_date')[:3]
    payment_list = Payment.objects.order_by('-pub_date')[:3]

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

def callAccountInput(request):
    type_in_list = TypeIncome.objects.order_by('-type_income')
    type_pay_list = TypePayment.objects.order_by('-type_payment')
    try:
       if(request.POST['choice'] == 'income'):
           choice = request.POST['choice']
           return render(request, 'ManMon/accountInput.html', {'type_in_list':type_in_list, 'choice':choice})
       else:
           return render(request, 'ManMon/accountInput.html', {'type_pay_list':type_pay_list, 'choice':choice})
    except:
       return render(request, 'ManMon/accountInput.html', '')

def saveAccount(request, choice):
    try:
        note = request.POST['note']
        money = request.POST['money']
        type_note = request.POST['type']
        date = request.POST['dmy']
    except:
        note = ""
        money = ""
        type_note = ""
        date = ""
    if(request.POST['choice'] == 'payment'):
        money = (-1)*money
    ac = Account(note = note, money = money, type_note = type_note, date = date)
    ac.save()

    return render(request, 'ManMon/saveAccount.html','')   

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
    
def callDelIncome(request):
    income_list = Income.objects.order_by('-pub_date')
    return render(request, 'ManMon/delIncome.html', {'income_list':income_list})

def delIncome(request, income_id):
    income = get_object_or_404(Income, pk=income_id)
    income.delete()    
    return render(request, "ManMon/main.html", '')

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

def delPayment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    payment.delete()
    return render(request, "ManMon/delPayment.html",'')

def callInsertType(request):
    return render(request,"ManMon/insertType.html",'')

def saveType(request):
    if(request.POST['choice'] == 'income' ):
        try:        
            save_type = request.POST['type']
        except:
            in_type = ""
        else:
            save_type = TypeIncome(type_income = save_type)
            save_type.save()
    if(request.POST['choice'] == 'payment' ):
        try:
            save_type = request.POST['type']
        except:
            save_type = ""
        else:
            save_type = TypePayment(type_payment = save_type)
            save_type.save()
    return render(request, "ManMon/saveType.html",{'save_type':save_type})
