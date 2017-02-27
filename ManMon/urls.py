from django.conf.urls import url

from . import views

app_name = 'ManMon'

urlpatterns = [
    url(r'^$', views.callMainPage, name='mainpage'),
    url(r'^accountinput$', views.callAccountInput, name='callAccountInput'),
    url(r'^(?P<choice>[a-z]+)/saveAccount$', views.saveAccount, name="saveAccount"),
    url(r'^history$', views.history, name='history'),
    url(r'^insertType/$', views.callInsertType, name='callInsertType'),
    url(r'^saveType/$', views.saveType, name='saveType'),
]
