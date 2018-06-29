# Ayomi_exercise-Django-
Candidature pour le poste de Développeur Full Stack

0. Envorionnement: 
   OS: Ubuntu 16.0.4 LTS
   Front-end: JQuery-1.10.2 Bootstrap-4.1.1  (chargés par CDN)
   Back-end: Python-2.7.12   Django-1, 8, 7

1. python manage.py runserver 0.0.0.0:8000
   *Faite attention de répertoire

2. http://127.0.0.1:8000/

3. Cliquez "S'inscrire" et entrer automatiquement http://127.0.0.1:8000/inscription

4. Remplissez la table et Cliquez le bouton "S'inscrire"

5. Vous êtes dans la page de "mon espace"  url:http://127.0.0.1:8000/insert_db

6. À votre gauche, c'est le pannel de function. Cliquez "Gerer mon compte"
	-Mes info
	-Modifier
	-Log out
7. D'abord on essaie "Mes info", il affiche les info remplits pendant l'inscription

8. En suite on clique Modifier, il vous permet de modifier votre E-mail
	-Remplissez nouveau E-mail et cliquer "Enregistrer"
	-Il va vous rappeler le nouveau E-mail que vous remplissez.
	-Si votre nouveau E-mail est bien enregistré, vous recevrez un autre rappele.
	 Ouvrez un nouvel onglet : http://127.0.0.1:8000/show_login et comparez le mél dans "Mes 	  info" dans le pannel à gauche
	 Cette function est réalisée par AJAX pour mettre à jour sans rechargement de la page.
9. Après on fait "Log out" pour se connecter deuxième fois, Vous revenez à l'accueil
   Mais on saisit imprudemment le compte incorrect dans cette fois. Il va rester dans la phase de  Sign in jusqu'à saisir bon compte ou s'inscrire.


@@
Auteur: ZHANG Chengjie
Contact: chengjie.zhang@utt.fr
Date: le 6 Juin 2018
Remarque:
C'est ma première fois d'utiliser django. C'est juste un demo simple fini dans 1 jour(effectivement 8 heures).
