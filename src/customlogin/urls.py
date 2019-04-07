from customlogin.views import *
from django.urls.conf import path


app_name = 'cl'
urlpatterns = [ 
    path('signup/',signup,name = 'signup'),
    path('signin/',signin,name = 'signin'),
    #127.0.0.1:8000/cl/signout
    path('signout/',signout,name = 'signout')
    ]