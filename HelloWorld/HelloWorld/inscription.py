# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
 
from django.http import HttpResponse
from Model_login.models import Login


def inscription_post2(request):
    ctx ={}
    ctx['login'] = request.POST.get('Login')
    ctx['mdp'] = request.POST.get('Mdp')
    ctx['prenom'] = request.POST.get('Prenom')
    ctx['nom'] = request.POST.get('Nom')
    ctx['mel'] = request.POST.get('Email')
    if request.method == "POST":
        Login.objects.create(
            login=request.POST.get("Login"), 
            mdp=request.POST.get("Mdp"), 
            nom=request.POST.get('Nom'),
            prenom=request.POST.get('Prenom'),
            mel=request.POST.get('Email')
        )
    return render(request, "mon_espace.html", {'ctx':ctx})

def inscription_form(request):
    return render(request, "inscription.html", {})

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