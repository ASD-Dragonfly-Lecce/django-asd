from django.shortcuts import render, get_object_or_404
from .models import Persona

def persona_list(request):
    persone = Persona.attivo.all()
    return render(request,
                  'persone/persona/list.html',
                  {'persone': persone})

def persona_detail(request, id):
    persona = get_object_or_404(Persona, id=id)
    return render(request,
                  'persone/persona/detail.html',
                  {'persona': persona})