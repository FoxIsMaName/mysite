from django.conf.urls import url

from . import views

app_name = 'ManMon'

urlpatterns = [
    url(r'^$', views.callMainPage, name='mainpage'),
    url(r'^accountinput$', views.callAccountInput, name='callAccountInput'),
    url(r'^saveAccount$', views.saveAccount, name="saveAccount"),
    url(r'^history$', views.history, name='history'),
    url(r'^exportHistory$', views.getCSV, name='getCSV'),
    url(r'^insertType/$', views.callInsertType, name='callInsertType'),
    url(r'^saveType/$', views.saveType, name='saveType'),
]
