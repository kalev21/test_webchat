from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>', views.room, name='room'),
    path('registers/', views.register, name='authorization'),
    path('loging/', views.user_login, name='enter'),
]
