from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def forecast_price(request):
    # TODO: conectar con src/ts/infer.py (ARIMA/Prophet)
    return JsonResponse({
        "ticker": request.GET.get("ticker", "MSFT"),
        "horizon_days": int(request.GET.get("h", 5)),
        "yhat": [100.1, 100.4, 100.2, 100.8, 101.0],
        "yhat_lower": [98.9, 99.2, 99.1, 99.5, 99.7],
        "yhat_upper": [101.3, 101.6, 101.4, 102.1, 102.4],
    })

def forecast_volatility(request):
    # TODO: conectar con src/ts/infer.py (GARCH)
    return JsonResponse({
        "ticker": request.GET.get("ticker", "MSFT"),
        "horizon_days": int(request.GET.get("h", 5)),
        "sigma_path": [0.18, 0.182, 0.179, 0.181, 0.183],
    })
