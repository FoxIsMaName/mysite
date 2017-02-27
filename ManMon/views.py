from django.shortcuts import render
from django.utils import timezone
from .models import Income, Payment, TypeIncome, TypePayment
from .models import Account

# Create your views here.

def callMainPage(request): 
    account_list = Account.objects.order_by('-pub_date')

    #calulation the rest of money
    remain_money = 0
    for account in account_list :
        remain_money += account.money

    account_list = Account.objects.order_by('-pub_date')[:3]
    return render(request, 'ManMon/main.html',{'remain_money':remain_money,         
                  'account_list':account_list})

def callAccountInput(request):
    type_in_list = TypeIncome.objects.order_by('-type_income')
    type_pay_list = TypePayment.objects.order_by('-type_payment')
    try:
       if(request.POST['choice'] == 'income'):
           choice = request.POST['choice']
           return render(request, 'ManMon/accountInput.html', {'type_in_list':type_in_list, 'choice':choice})
       else:
           choice = request.POST['choice']
           return render(request, 'ManMon/accountInput.html', {'type_pay_list':type_pay_list, 'choice':choice})
    except:
       return render(request, 'ManMon/chooseInOrPay.html', '')

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
    if(choice == 'payment'):
        money = (-1)*float(money)

    ac = Account(note = note, money = money, type_note = type_note, pub_date = date)
    ac.save()
    return render(request, 'ManMon/saveAccount.html',{'note':note, 'money':money, 'type_note':type_note, 'date':date})
   
def history(request):
    account_list = Account.objects.order_by('-pub_date')
    money_sum = 0
    for account in account_list :
        money_sum += account.money
    return render(request, 'ManMon/history.html', {'account_list':account_list, 'money_sum':money_sum})

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
