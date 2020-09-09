from django.shortcuts import render
from .forms import ReservaForm,VisitaForm,VisitaRealForm
from .models import Persona,Visita
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        #form.fields['tile'].queryset = Tile.objects.filter(section__xxx=yyy)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'listo.html', {'form': form})
        else:
            print('Error')

            return render(request, 'error.html', {'form': form})

    else:
        form = ReservaForm()
        return render(request,'index.html',{'form':form})



def visita2(request):
    if request.method == "POST":
        form = VisitaForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'listo_bienvenido.html', {'form': form})
        else:
            print('Error')

            return render(request, 'error.html', {'form': form})

    else:
        form = VisitaForm()
        return render(request,'visita.html',{'form':form})



def visita(request):

    if request.method == "POST":
        form = VisitaForm(request.POST)
        try:
            persona = Persona.objects.get(cedula_persona=form['cedula_persona'].value())
        except Exception as e :
            if form.is_valid():
                persona = form.save(commit=False)
                persona.save()

        persona = Persona.objects.get(cedula_persona=form['cedula_persona'].value())

        new_visita = Visita()
        new_visita.fechahora_visita = timezone.now()
        new_visita.persona = persona
        new_visita.save(force_insert=True)
        return render(request, 'listo_bienvenido.html', {'form': form})

    else:
        form = VisitaForm()
        return render(request, 'visita.html', {'form': form})


@login_required(login_url='/manage')
def listPersonasSinMesa(request):
    listVisita = Visita.objects.filter(activo=True,mesa_asignada__isnull=True)
    return render(request,'lista_persona.html',
                  {'listVisita': listVisita})


def asigtable(request):
    listaPersonas = request.GET.get('listp')
    mesaAsig = request.GET.get('table')

    visita = Visita.objects.get(persona__cedula_persona__exact=listaPersonas,activo=True)

    visita.mesa_asignada = mesaAsig

    visita.save()

    return HttpResponse('Listo')