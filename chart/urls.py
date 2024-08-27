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
    path('ssgInC/', ssg_detail_view,name="ssg-index"),
    path('lotteino/', lotteino_detail_view,name="lotteino-index"),
    path('naver/', naver_detail_view,name="naver-index"),
    path('posco/', posco_detail_view,name="posco-index"),
    path('poscodx/', poscodx_detail_view,name="poscodx-index"),
    path('hyundaiauto/', hyundaiauto_detail_view,name="hyundaiauto-index"),
    path('ssSDI/', ssSDI_detail_view,name="ssSDI-index"),
    path('ssElec/', ssElec_detail_view,name="ssElec-index"),
    path('skhynix/', skhynix_detail_view,name="skhynix-index"),
    path('hyundaidp/', hyundaidp_detail_view,name="hyundaidp-index"),
    path('hanhwasys/', hanhwasys_detail_view,name="hanhwasys-index"),
    path('skinc/', skinc_detail_view,name="skinc-index"),

]