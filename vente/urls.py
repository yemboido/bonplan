from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/$',views.articles,name='articles'),
    url(r'^offre/$', views.Offre, name='offre'),
    url(r'^connexion/$',views.connexion,name='Connexion'),
    url(r'^contact/$',views.deconnexion,name='deconnexion'),
    url(r'^inscription/$',views.inscription,name='inscription'),
    url(r'^articles/(?P<id>\d+)/$',views.lire,name='lire'),
]
