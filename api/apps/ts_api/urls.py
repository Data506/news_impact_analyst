from django.urls import path
from . import views


urlpatterns = [
    path('price/', views.forecast_price, name='forecast_price'),
    path('volatility/', views.forecast_volatility, name='forecast_volatility'),
]