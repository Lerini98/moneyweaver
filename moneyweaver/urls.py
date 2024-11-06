from django.urls import path
from .views import *

# app.urls.py -> request & view를 연결해줌
urlpatterns = [
    # localhost/user/ + ''
    path('', index, name="moneyweaver-index"),
    path('intro/', intro, name="moneyweaver-intro"),
    path('intro/popup/', popup, name="moneyweaver-popup")
]