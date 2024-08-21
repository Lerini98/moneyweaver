from django.urls import path
from .views import kt_detail_view,lg_detail_view,ssSDS_detail_view

# app.urls.py -> request & view를 연결해줌
urlpatterns = [
    # localhost/user/ + ''
    path('kt/', kt_detail_view, name="kt-index"),
    path('lg/', lg_detail_view,name="lg-index"),
    path('ssSDS/', ssSDS_detail_view,name="ssSDS-index")
]