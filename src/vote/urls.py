from django.urls.conf import path
from vote.views import *

app_name = 'vote'
urlpatterns = [
    #127.0.0.1:8000/vote/
    path('', index, name = 'index'),
    #127.0.0.1:8000/vote/숫자/
    path('<int:q_id>/',detail, name = 'detail'),
    #127.0.0.1:8000/vote/result/숫자/
    path('result/<int:q_id>/',result, name = 'result'),
    #127.0.0.1:8000/vote/qr/
    path('qr/', qregister, name = 'qregister'),
    #127.0.0.1:8000/vote/qu/숫자
    path('qu/<int:q_id>/',qupdate, name = 'qupdate'),
    #127.0.0.1:8000/vote/qd/숫자
    path('qd/<int:q_id>/',qdelete, name = 'qdelete'),
    path('cr/',cregister, name = 'cregister'),
    path('cu/<int:c_id>/',cupdate, name = 'cupdate'),
    path('cd/<int:c_id>/',cdelete, name = 'cdelete'),
    ] 