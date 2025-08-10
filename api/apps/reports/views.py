from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def daily_report(request):
    # TODO: juntar nlp + ts y formar informe
    return JsonResponse({
        "ticker": request.GET.get("ticker", "AAPL"),
        "top_news": [{"title": "Earnings beat", "impact": "positive"}],
        "signals": {"price_trend": "up", "volatility": "moderate"},
    })
