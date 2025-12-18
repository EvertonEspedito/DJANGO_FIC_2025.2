from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required




def grupo_medico(user):
    return user.groups.filter(name='Médico').exists()

@login_required
def dashboard(request):
    context = {
        'total': Paciente.objects.count(),
        'urgentes': Paciente.objects.filter(prioridade='U').count(),
        'altos': Paciente.objects.filter(prioridade='A').count(),
        'medios': Paciente.objects.filter(prioridade='M').count(),
        'baixos': Paciente.objects.filter(prioridade='B').count(),
    }
    return render(request, 'saude/dashboard.html', context)


@login_required
@user_passes_test(grupo_medico)
def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('listar_pacientes')

@login_required
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'saude/listar.html', {'pacientes': pacientes})

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'saude/listar.html', {'pacientes': pacientes})

def cadastrar_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pacientes')
    return render(request, 'saude/form.html', {'form': form})

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('listar_pacientes')
    return render(request, 'saude/form.html', {'form': form})

def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('listar_pacientes')

def listar_pacientes(request):
    pacientes = Paciente.objects.all().order_by('-prioridade', 'data_consulta')
    return render(request, 'saude/listar.html', {'pacientes': pacientes})

@permission_required('saude.add_paciente')
def cadastrar_paciente(request):
    ...

@permission_required('saude.change_paciente')
def editar_paciente(request, id):
    ...

@permission_required('saude.delete_paciente')
def excluir_paciente(request, id):
    ...

@permission_required('saude.change_paciente')
def confirmar_atendimento(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.atendido = True
    paciente.save()
    return redirect('listar_pacientes')

@permission_required('saude.view_paciente')
def relatorio_atendidos(request):
    pacientes = Paciente.objects.filter(atendido=True).order_by('-data_consulta')
    return render(request, 'saude/relatorio.html', {'pacientes': pacientes})
