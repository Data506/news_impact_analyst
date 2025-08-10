from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.classify_news, name='classify_news'),
]