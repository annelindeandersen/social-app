from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(10)
    send_mail('Welcome to the feed', 
    'You have signed up', 
    'annelindea@gmail.com', 
    ['annelindea@gmail.com'])
    return None