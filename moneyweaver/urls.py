from django.urls import path
from .views import index

# app.urls.py -> request & view를 연결해줌
urlpatterns = [
    # localhost/user/ + ''
    path('', index, name="moneyweaver-index")
]