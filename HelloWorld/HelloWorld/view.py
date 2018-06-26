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
    return render(request, 'hello.html', context)

class User:
    def __init__(self, login, mdp):
      self.login = login
      self.mdp = mdp
      self.nom = "init"
      self.prenom = "init"
      self.mel = "init@init.com"

    #entrer la page de s'inscrire
    def inscription_form(self,request):
        return render(request, "inscription.html", {})
    #entrer la page qui confirme la succes de l'inscription
    def inscription_DB(self,request):
        ctx ={}
        if request.method == "POST":
            Login.objects.create(
                login=request.POST.get("Login"), 
                mdp=request.POST.get("Mdp"), 
                nom=request.POST.get('Nom'),
                prenom=request.POST.get('Prenom'),
                mel=request.POST.get('Email')
            )
        return render(request, "insc_index.html", {'ctx':ctx})
    #se connecter, entrer la page "mon_espace" si correcte
    def sign_in(self,request):
        self.login=request.POST['login']
        self.mdp=request.POST['mdp']
        id = Login.objects.filter(login=self.login, mdp=self.mdp)
        if id:
            champs = ['login','mdp','nom','prenom','mel']
            context = {}
            context['user'] = self
            for field in champs:
                context[field] = id.values(field).first().get(field)

            return render(request, "mon_espace.html", {'ctx':context})
        else:
            return render(request, "hello.html", {'sign_error':'Compte n\'est pas correcte'})



def show_Login(request):
    response = "*-ID*-Login*-Mot de passe*-nom*-prenom*-mel<br>"
    list = Login.objects.all() 
    for var in list:
        response +="*-"+ str(var.id) + "*-" + var.login + "*-" + var.mdp +"*-"+var.nom+"*-"+var.prenom+"*-"+var.mel + "!<br>"
    return HttpResponse("<p>" + response + "</p>")

def delete_Login(request):
    response = "*-ID*-Login*-Mot de passe*-nom*-prenom*-mel<br>"
    Login.objects.all().delete()
    return HttpResponse("<p>" + response + "</p>")



def ajax_submit(request):
    if request.method=="POST":
        update = Login.objects.filter(login=request.POST['login'],mdp=request.POST['mdp']).first()
        update.mel = request.POST['mel']
        update.save()
        return HttpResponse("Please compare information in 'Mes info' and 'Modifier' in the lefthand, furthur more check Model_login: http://127.0.0.1:8000/show_login")

    