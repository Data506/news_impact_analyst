from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def ingest_news(request):
    return JsonResponse({"status": "ok", "message": "Ingesta de noticias iniciada"})