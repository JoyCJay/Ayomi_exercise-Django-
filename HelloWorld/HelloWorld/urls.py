"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
'''
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
'''

from django.conf.urls import include, url
 
import view

user1 = view.User("id", "mot de passe")
 
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^inscription$', user1.inscription_form),
    url(r'^insc_index$', user1.inscription_DB),
    url(r'^mon_espace$', user1.sign_in),
    url(r'^test_ajax$', view.ajax_submit),

    url(r'^show_login$', view.show_Login),
    url(r'^delete_login$', view.delete_Login),
]
