from django.urls import path, include

from . import views
from rest_framework import routers
router =  routers.DefaultRouter()
router.register('users', views.UserView)

app_name = 'loginapp'

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    # path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('password_reset', views.password_reset, name='password_reset'),
]