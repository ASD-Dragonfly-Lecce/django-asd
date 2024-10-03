from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Persona


class PersonaListView(ListView):
    queryset = Persona.attivo.all()
    context_object_name = 'persone'
    paginate_by = 1
    template_name = 'persone/persona/list.html'


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