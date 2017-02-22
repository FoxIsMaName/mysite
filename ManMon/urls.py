from django.conf.urls import url

from . import views

app_name = 'ManMon'

urlpatterns = [
    url(r'^$', views.callMainPage, name='mainpage'),
    url(r'^insertincome$', views.callInsertIncome, name='callInsertIncome'),
    url(r'^insertpayment$', views.callInsertPayment, name='callInsertPayment'),
    url(r'^saveincome$', views.saveIncome, name='saveIncome'),
    url(r'^savepayment$', views.savePayment, name='savePayment'),
    url(r'^income/$', views.tableIncome, name='showIncome'),
    url(r'^payment/$', views.tablePayment, name='showPayment'),    
]
