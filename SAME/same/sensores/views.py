from django.shortcuts import render, redirect, get_object_or_404
from .models import Leitura

def list_leituras(request):
    leituras = Leitura.objects.all().order_by('-data_hora')
    return render(request, "leituras/list.html", {"leituras": leituras})


def create_leitura(request):
    if request.method == "POST":
        temperatura = request.POST.get("temperatura")
        umidade = request.POST.get("umidade")

        Leitura.objects.create(
            temperatura=temperatura,
            umidade=umidade
        )

        return redirect("list_leituras")

    return render(request, "leituras/create.html")


def edit_leitura(request, id):
    leitura = get_object_or_404(Leitura, id=id)

    if request.method == "POST":
        leitura.temperatura = request.POST.get("temperatura")
        leitura.umidade = request.POST.get("umidade")
        leitura.save()

        return redirect("list_leituras")

    return render(request, "leituras/edit.html", {"leitura": leitura})


def delete_leitura(request, id):
    leitura = get_object_or_404(Leitura, id=id)
    leitura.delete()
    return redirect("list_leituras")

def dashboard(request):
    return render(request, "dashboard.html")
