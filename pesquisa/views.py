from django.shortcuts import render

from . models import Pergunta
# Create your views here.

def index(request):
    todas = Pergunta.objects.all()  #retorna todas as perguntas cadastradas
    return render(request, 'index.html',{
        "perguntas": todas #volta o valor da variavel todas que foi passado acima , dicionario.

    })