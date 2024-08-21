from django.urls import path
from .views import company_detail_view

# app.urls.py -> request & view를 연결해줌
urlpatterns = [
    # localhost/user/ + ''
    path('', company_detail_view, name="kt-index")
]