from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.test),
    path('sendmails', views.send_mail_to_all),
]
