'''
from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")
'''
from django.shortcuts import render
from django.views.decorators import csrf
 
from django.http import HttpResponse
from Model_login.models import Login
 
def hello(request):
    context = {}
    context['hello'] = 'Hello Visitor!'
    context['github'] = 'Microsoft is acquiring GitHub!:('
    return render(request, 'hello.html', context)

def sign_in(request):
    id = Login.objects.filter(login=request.POST['login'],mdp=request.POST['mdp'])
    if id:
        champs = ['login','mdp','nom','prenom','mel']
        context = {}
        for field in champs:
            context[field] = id.values(field).first().get(field)

        return render(request, "mon_espace.html", {'ctx':context})
    else:
        return render(request, "hello.html", {'sign_error':'Compte n\'est pas bon'})
        
def ajax_submit(request):
    if request.method=="POST":
        update = Login.objects.filter(login=request.POST['login'],mdp=request.POST['mdp']).first()
        update.mel = request.POST['mel']
        update.save()
        return HttpResponse("Please compare information in 'Mes info' and 'Modifier' in the lefthand, furthur more check Model_login: http://127.0.0.1:8000/show_login")

    