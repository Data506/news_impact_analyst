from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.ingest_news, name='ingest_news'),
]