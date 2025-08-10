from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(["POST"])
def chat_with_analyst(request):
    """
    Endpoint de ejemplo para interactuar con el analista virtual.
    Por ahora devuelve una respuesta fija.
    """
    try:
        body = json.loads(request.body.decode("utf-8")) if request.body else {}
        question = body.get("question", "")
        response = {
            "question": question,
            "answer": "Este es un placeholder. Aquí irá la lógica del LLM."
        }
        return JsonResponse(response, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
