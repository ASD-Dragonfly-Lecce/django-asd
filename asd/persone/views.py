from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Persona, Timbratura
from .forms import TesseratoForm, TimbraturaForm


class PersonaListView(ListView):
    queryset = Persona.attivo.all()
    context_object_name = 'persone'
    paginate_by = 1
    template_name = 'persona/list.html'


def persona_list(request):
    object_list = Persona.attivo.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try:
        persone = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        persone = paginator.page(1)
    except EmptyPage:
        persone = paginator.page(paginator.num_pages)
    return render(request,
                  'persona/list.html',
                  {'page': page,
                      'persone': persone})

def persona_detail(request, id):
    persona = get_object_or_404(Persona, id=id)
    return render(request,
                  'persona/detail.html',
                  {'persona': persona})


def tesserato_new(request):
    
    new_tesserato = None

    if request.method == 'POST':
        form = TesseratoForm(data=request.POST)
        if form.is_valid():
            new_tesserato = form.save(commit=False)
            new_tesserato.save()
    else:
        form = TesseratoForm()
    return render(request, 'persona/new.html', {
        'form': form,
        'new_tesserato': new_tesserato,
    })


@login_required
def timbratura_new(request):
    new_timbratura = None
    timbrature_odierne = Timbratura.odierne.all()

    if request.method == 'POST':
        form = TimbraturaForm(data=request.POST)
        if form.is_valid():
            new_timbratura = form.save(commit=False)
            new_timbratura.utente = request.user
            new_timbratura.save()
            messages.success(request, 'Registrazione completata')
            return redirect('/persone/timbratura')
    else:
        form = TimbraturaForm()
    return render(request, 'persona/timbratura.html', {
        'form': form,
        'new_timbratura': new_timbratura,
        'timbrature_odierne': timbrature_odierne,
    })

