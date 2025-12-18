from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Leitura

@csrf_exempt
def receber_leitura(request):
    if request.method == "POST":
        data = json.loads(request.body)

        leitura = Leitura.objects.create(
            temperatura=data["temperatura"],
            umidade=data["umidade"]
        )

        return JsonResponse({"status": "ok"})

    if request.method == "GET":
        leituras = list(
            Leitura.objects.values("id", "temperatura", "umidade", "data_hora")
            .order_by("-data_hora")
        )
        return JsonResponse(leituras, safe=False)
