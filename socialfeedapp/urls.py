from django.urls import path
# from .views import PostListView

from . import views


app_name = 'socialfeedapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('groups', views.groups, name='groups'),
    path('base', views.base, name='base'),
    path('join_group/<int:pk>', views.join_group, name='join_group'),
    path('leave_group/<int:pk>', views.leave_group, name='leave_group'),
    # path('details/<int:pk>', views.details, name='details'),
    path('profile', views.profile, name='profile'),
]