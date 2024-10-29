from django.urls import path
from .views import *
# app.urls.py -> request & view를 연결해줌
urlpatterns = [
    # localhost/user/ + ''
   
    path('index/skhynix/', skhynix_detail_view,name="skhynix-index"),
    path('index/skinc/', skinc_detail_view,name="skinc-index"),
    path('index/', chartindex, name="chartindex"),
    # path('charts/',chart, name="chart")

]