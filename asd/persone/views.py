from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Persona


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
                  'persone/persona/list.html',
                  {'page': page,
                      'persone': persone})

def persona_detail(request, id):
    persona = get_object_or_404(Persona, id=id)
    return render(request,
                  'persone/persona/detail.html',
                  {'persona': persona})