from django.urls import path
from chat import views
app_name = 'chat'

urlpatterns = [
path('',views.HomeView, name='home'),
path('<str:room_name>/', views.ChatRoom, name='chat_room'),  
]
