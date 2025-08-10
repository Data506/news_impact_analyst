from django.urls import path
from . import views


urlpatterns = [
    path('daily/', views.daily_report, name='daily_report'),
]