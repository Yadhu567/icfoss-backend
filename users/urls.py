from django.urls import path 
from . import views

app_name= 'users'

urlpatterns=[
   path('signin/',views.signin,name='signin'),
   path('signup/',views.signup,name='signup'),
   path('reset/',views.reset,name='reset')
]