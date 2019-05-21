from django.shortcuts import render
from appTicket.forms import BandaForm

# Create your views here.

# função pra chamar o arquivo html 
def main(request):
    formulario = BandaForm(request.POST or None)
    msg = ''
    if formulario.is_valid():
        formulario.save()
        formulario= BandaForm()
        msg= 'Analisaremos o perfil e entraremos em contato!'

    contexto = {
        'form': formulario,
        'msg': msg
    }

    return render(request, 'main.html', contexto)

def shows(request):
    return render(request,'shows.hmtl')
