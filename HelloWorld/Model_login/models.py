# models.py
from django.db import models
 
class Login(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=20)
    mdp = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    mel = models.CharField(max_length=40)