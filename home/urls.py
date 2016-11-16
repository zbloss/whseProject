from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^incoming/$', views.incoming, name="incoming"),
    url(r'^outgoing/$', views.outgoing, name="outgoing"),
    url(r'^addincoming/$', views.addIncoming, name="addIncoming"),
]
