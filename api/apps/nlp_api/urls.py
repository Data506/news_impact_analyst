from django.urls import path
from . import views

urlpatterns = [
    path('sentiments/', views.classify_news, name='classify_news'),
]