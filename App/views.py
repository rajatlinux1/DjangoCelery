from django.http import HttpResponse
from django.shortcuts import render

from App.task import test_func
from email_work.task import send_mail_fun

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done2 ")


def send_mail_to_all(request):
    send_mail_fun.delay()
    return HttpResponse("Sent")