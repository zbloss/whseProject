from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^incoming/$', views.incoming, name="incoming"),
    url(r'^incoming/ithankyou/$', views.ithankyou, name="incomingThankYou"),
    url(r'^outgoing/$', views.outgoing, name="outgoing"),
    url(r'^outgoing/othankyou/$', views.othankyou, name="outgoingThankYou"),
    url(r'^containers/$', views.containers, name="containers"),
]
