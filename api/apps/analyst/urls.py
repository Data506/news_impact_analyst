from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_with_analyst, name='chat_with_analyst'),
]