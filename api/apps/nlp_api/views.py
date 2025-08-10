from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(["POST"])
def classify_news(request):
    """
    Stub: recibe {"text": "...", "ticker": "AAPL"} y devuelve un JSON fijo.
    Luego conectaremos con src/nlp/infer.py
    """
    try:
        body = json.loads(request.body.decode("utf-8")) if request.body else {}
        text = body.get("text", "")
        ticker = body.get("ticker")
        # TODO: llamar a tu pipeline real de NLP
        result = {
            "topic": "earnings",
            "sentiment": "positive",
            "impact_score": 0.72,
            "confidence": 0.80,
            "echo": {"ticker": ticker, "len_text": len(text)}
        }
        return JsonResponse(result, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
