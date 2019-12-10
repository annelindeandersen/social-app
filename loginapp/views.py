from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponse
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

from .utils import random_string
from .tasks import sleepy, send_email_task
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
# from .middleware import SetLastVisitMiddleware


def login(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(request, 
            username=request.POST['user'], 
            password=request.POST['password'])
        if user:
            dj_login(request, user)
            # last_login = SetLastVisitMiddleware()
            # last_login.save()
            return HttpResponseRedirect(reverse('socialfeedapp:index'))
        else:
            #context = {'error':'Username or password is wrong.'}
            context['error'] = 'Username or password is wrong.'

    return render(request, 'loginapp/login.html', context)

def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('loginapp:login'))


def signup(request):
    if User.is_authenticated:
        dj_logout(request)
    context = {}
    if request.method == 'POST':
        if not request.POST['password'] == request.POST['repeatpassword']:
            context['error'] = 'Passwords do not match.'
            return render(request, 'loginapp/signup.html', context)
        if len(User.objects.filter(username=request.POST['user'])) > 0:
            context['error'] = 'Username already exists.'
            return render(request, 'loginapp/signup.html', context)
        if len(User.objects.filter(email=request.POST['email'])) > 0:
            context['error'] = 'Email already exists.'
            return render(request, 'loginapp/signup.html', context)
        user = User.objects.create_user(request.POST['user'],password=request.POST['password'], email=request.POST['email'])
        user.save()
        send_email_task.delay()
        dj_login(request, user)
        return HttpResponseRedirect(reverse('socialfeedapp:index'))

    return render(request, 'loginapp/signup.html')


def password_reset(request):
    context = {}
    if request.method == 'POST':
        users = User.objects.filter(username=request.POST['user'])
        if users:
            user = users[0]
            new_password = random_string()
            user.set_password(new_password)
            user.save()
            print(f'**** User {user} change password to {new_password}')
            return HttpResponseRedirect(reverse('loginapp:login'))
        else:
            context['error'] = 'No such username.'
        
    return render(request, 'loginapp/password_reset.html', context)


# @login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            # return HttpResponseRedirect(reverse('profile'))
            return HttpResponseRedirect(request.path_info)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'loginapp/profile.html', context)




def email(request):
    send_email_task.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY</H1>')



# for the rest api
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # allow POST, GET, PUT etc
    permissions.classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer