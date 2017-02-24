from django.conf.urls import url

from . import views

app_name = 'ManMon'

urlpatterns = [
    url(r'^$', views.callMainPage, name='mainpage'),
    url(r'^accountinput$', views.callAccountInput, name='accountInput'),
    url(r'^typeInput$', views.callTypePage, name="typePage"),
    url(r'^insertincome$', views.callInsertIncome, name='callInsertIncome'),
    url(r'^insertpayment$', views.callInsertPayment, name='callInsertPayment'),
    url(r'^saveincome$', views.saveIncome, name='saveIncome'),
    url(r'^savepayment$', views.savePayment, name='savePayment'),
    url(r'^income/$', views.tableIncome, name='showIncome'),
    url(r'^payment/$', views.tablePayment, name='showPayment'),
    url(r'^insertType/$', views.callInsertType, name='callInsertType'),
    url(r'^saveType/$', views.saveType, name='saveType'),
    url(r'^deleteIncome/$', views.callDelIncome, name='callDelIncome'),
    url(r'^deletedIncome/$', views.delIncome, name='delIncome'),
    url(r'^deletePayment/$', views.delPayment, name='delPayment'),
]
