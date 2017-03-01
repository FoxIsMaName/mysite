import csv
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Account, TypeIncome, TypePayment

# Create your views here.

def callMainPage(request): 
    account_list = Account.objects.order_by('-pub_date')

    #calulation the rest of money
    remain_money = 0
    for account in account_list :
        remain_money += account.money

    account_list = Account.objects.order_by('-pub_date')[:5]
    return render(request, 'ManMon/main.html',{'remain_money':remain_money,         
                  'account_list':account_list})

def callAccountInput(request):
    type_in_list = TypeIncome.objects.order_by('-type_income')
    type_pay_list = TypePayment.objects.order_by('-type_payment')

    return render(request, 'ManMon/accountInput.html', {'type_in_list':type_in_list,'type_pay_list':type_pay_list})

def saveAccount(request):
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

def getCSV(request):
    account_list = Account.objects.order_by('pub_date')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ManMon.csv"'

    writer = csv.writer(response)
    writer.writerow(['note', 'money', 'type', 'date'])
    for account in account_list :
        writer.writerow([account.note, account.money, account.type_note, account.pub_date])

    return response
