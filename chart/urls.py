from django.urls import path
from .views import *
# app.urls.py -> request & view를 연결해줌
urlpatterns = [
    # localhost/user/ + ''
    path('',index,name="chart-index"),
    path('index/kt/', kt_detail_view, name="kt-index"),
    path('index/lg/', lg_detail_view,name="lg-index"),
    path('index/ssSDS/', ssSDS_detail_view,name="ssSDS-index"),
    path('index/hyundai/', hd_detail_view,name="hyundai-index"),
    path('index/kakao/', kakao_detail_view,name="kakao-index"),
    path('index/ssgInC/', ssg_detail_view,name="ssg-index"),
    path('index/lotteino/', lotteino_detail_view,name="lotteino-index"),
    path('index/naver/', naver_detail_view,name="naver-index"),
    path('index/posco/', posco_detail_view,name="posco-index"),
    path('index/poscodx/', poscodx_detail_view,name="poscodx-index"),
    path('index/hyundaiauto/', hyundaiauto_detail_view,name="hyundaiauto-index"),
    path('index/ssSDI/', ssSDI_detail_view,name="ssSDI-index"),
    path('index/ssElec/', ssElec_detail_view,name="ssElec-index"),
    path('index/skhynix/', skhynix_detail_view,name="skhynix-index"),
    path('index/hyundaidp/', hyundaidp_detail_view,name="hyundaidp-index"),
    path('index/hanhwasys/', hanhwasys_detail_view,name="hanhwasys-index"),
    path('index/skinc/', skinc_detail_view,name="skinc-index"),
    path('index/', chartindex, name="chartindex"),
    path('charts/',chart, name="chart")

]