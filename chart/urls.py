from django.urls import path
from .views import *
# app.urls.py -> request & view를 연결해줌
urlpatterns = [
    # localhost/user/ + ''
    path('',index,name="chart-index"),
    path('kt/', kt_detail_view, name="kt-index"),
    path('lg/', lg_detail_view,name="lg-index"),
    path('ssSDS/', ssSDS_detail_view,name="ssSDS-index"),
    path('hyundai/', hd_detail_view,name="hyundai-index"),
    path('kakao/', kakao_detail_view,name="kakao-index"),
    path('ssgInC/', ssg_detail_view,name="ssg-index")
]