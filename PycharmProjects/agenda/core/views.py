from django.shortcuts import render
from core.models import Evento

# Create your views here.

def lista_eventos(request):

    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request,'agenda.html', dados)

#def index(request):
#    return redirect('/agenda/')