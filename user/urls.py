from django.urls import path
from user.views import board_list, board_detail, board_write, delete
#from .import views

# app_name = 'user'

urlpatterns = [
    path('', board_list, name='board_list'), 
    path('blog/', board_write, name='board_write'), 
    path('<int:pk>/', board_detail, name='board_detail'),
    path('<int:pk>/delete/', delete, name = "delete")
]