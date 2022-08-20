from django.urls import path 
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('home/',home,name='home'),
    path('sign_up/',RegisterPage.as_view(),name='sign_up'),
    path('logout/',LogoutView.as_view(template_name = 'base/logout.html'),name='logout'),
]