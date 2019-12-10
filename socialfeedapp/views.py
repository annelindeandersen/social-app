from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import FeedPost, AppGroup
from . import models


@login_required
def index(request):
    user = User.objects.filter(pk=1)[0]
    # user = User.objects.filter(user=request.user)

    if request.method == 'GET':
        user_groups = models.AppGroup.objects.filter(users__username__contains=user.username)
        print(user, user_groups)
        posts = models.FeedPost.objects.filter(group__in=user_groups).order_by('-created')[:10]

        context = {
            'user': user,
            'posts': posts,
            'user_groups': user_groups,
        }

        return render(request, 'socialfeedapp/index.html', context=context)

    if request.method == 'POST':
        post = models.FeedPost()
        post.title = request.POST['title']
        post.description = request.POST['text']
        post.group = models.AppGroup.objects.get(pk=request.POST['group'])
        post.user = request.user
        post.save()
        return HttpResponseRedirect(reverse('socialfeedapp:index'))

    return HttpResponseBadRequest()

def groups(request):
    user = User.objects.filter(pk=1)[0]
    # user = User.objects.filter(user=request.owner)
    if request.method == 'GET':
        user_groups = models.AppGroup.objects.filter(users__username__contains=user.username)
        not_user_groups = models.AppGroup.objects.exclude(users__username__contains=user.username)

        context = {
            'user_groups': user_groups,
            'not_user_groups': not_user_groups,
            'user': user,
        }

        return render(request, 'socialfeedapp/groups.html', context=context)

    if request.method == 'POST':
        group = models.AppGroup()
        group.name = request.POST['name']
        group.description = request.POST['description']
        group.owner = request.user
        group.save()
        group.users.add(user)
        group.save()
        return HttpResponseRedirect(reverse('socialfeedapp:groups'))

    return HttpResponseBadRequest()


def join_group(request, pk):
    user = User.objects.filter(pk=1)[0]
    # user = User.objects.filter(user=request.user)
    group = models.AppGroup.objects.get(pk=pk)
    group.users.add(user)
    group.save()
    return HttpResponseRedirect(reverse('socialfeedapp:groups'))


def leave_group(request, pk):
    user = User.objects.filter(pk=1)[0]
    # user = User.objects.filter(user=request.user)
    group = models.AppGroup.objects.get(pk=pk)
    group.users.remove(user)
    group.save()
    return HttpResponseRedirect(reverse('socialfeedapp:groups'))


def profile(request):
    pass

def base(request):
    # return HttpResponseRedirect(reverse('socialfeedapp:base'))
    return render(request, 'socialfeedapp/base.html')







########################################################### GAMLE

# def index(request):
#     if request.method == 'GET':
#         feed_posts = FeedPost.objects.all()
#         context = {
#             'posts': feed_posts
#         }
#         return render(request, 'socialfeedapp/index.html', context)

#     if request.method == 'POST':
#         feed_post = FeedPost()
#         feed_post.title = request.POST['title']
#         feed_post.description = request.POST['description']
#         feed_post.status = False
#         feed_post.user = request.user
#         feed_post.save()
#         return HttpResponseRedirect(reverse('socialfeedapp:index'))

#     return HttpResponseBadRequest()


# @login_required
# def profile(request):
#     if request.method == 'GET':
#         feed_posts = FeedPost.objects.filter(user=request.user)
#         context = {
#             'posts': feed_posts
#         }
#         return render(request, 'socialfeedapp/profile.html', context)

#     if request.method == 'POST':
#         feed_post = FeedPost()
#         feed_post.title = request.POST['title']
#         feed_post.description = request.POST['description']
#         feed_post.status = False
#         feed_post.user = request.user
#         feed_post.save()
#         return HttpResponseRedirect(reverse('socialfeedapp:profile'))

#     return HttpResponseBadRequest()

# @login_required
# def details(request, pk):
#     post = get_object_or_404(FeedPost, pk=pk, user=request.user)

#     if request.method == 'GET':
#         context = {
#             'post': post
#         }
#         return render(request, 'socialfeedapp/details.html', context)

#     if request.method == 'POST':
#         post.title = request.POST['title']
#         post.description = request.POST['description']
#         status = request.POST.getlist('status')
#         if len(status) > 0:
#             post.status = True
#         else:
#             post.status = False
#         post.save()
#         return HttpResponseRedirect(reverse('socialfeedapp:index'))

#     return HttpResponseBadRequest()

# def groups(request):
#     # return HttpResponseRedirect(reverse('socialfeedapp:groups'))
#     return render(request, 'socialfeedapp/groups.html')