from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
# import yagmail


def index(request):
    return HttpResponse("Hello, world. You're at the emails index.")

class EmailView(TemplateView):
    template_name = 'emailapp/email.html'


# receiver = "annelindea@gmail.com"
# body = "Hello there from Yagmail"
# filename = "document.pdf"

# yag = yagmail.SMTP("annelindea@gmail.com")
# yag.send(
#     to=receiver,
#     subject="Yagmail test with attachment",
#     contents=body, 
#     attachments=filename,
# )

# from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'annelindea@gmail.com',
#     ['annelindea@gmail.com'],
#     fail_silently=False,
# )