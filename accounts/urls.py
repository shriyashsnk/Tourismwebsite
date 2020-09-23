from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns=[
    path('register',views.register,name='Register'),
    path('login',views.login,name='login'),
   
    path('logout',views.logout,name='Logout')
]