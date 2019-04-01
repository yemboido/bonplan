from django.db import models
from django.utils import timezone
from django.core.files import File
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class  article(models.Model):
    pays=models.CharField(max_length=100)
    localite=models.CharField(max_length=100)
    choix=(( '1','offre'),
            ('2','demande') )
    type=models.CharField(max_length=2,choices=choix)
    
    choix2=( ('AUTO-MOTO',(('Voiture doccasion'),
             ('Motos'),
             ('Pièces et équipements'),
             ('Location'))),
             
             ('IMMOBILIER',(('Vente immobilier'),
             ('Location immobilier'))),
             
             ('Accessoires',(
             ('Bijoux et montres'),
             ('Chaussures'),
             ('Maroquinerie'),
             ('Vêtements'))),

             ('Electronique',(
             ('Consoles et jeux vidéos'),
             ('Matériel informatique'),
             ('Téléphones et tablettes'))),
             
             ('Service',(('Aide aux personnes dépendantes'),
             ('Animation mariage et fêtes'),
             ('Cours particulier / soutien scolaire'),
             ('Locations événementielles')))
             )          
    categories=models.CharField(choices=choix2)
    descriptions=models.TextField()
    prix=models.CharField(max_length=10)
    Numeros=models.CharField(max_length=10)
    photo1=models.ImageField(upload_to='images/')
    photo2=models.ImageField(upload_to='images/')
    photo3=models.ImageField(upload_to='images/')
    photo4=models.ImageField(upload_to='images/')
    date_publication= models.DateTimeField(default=timezone.now)



    def publish(self):
        self.date_publication = timezone.now()
        self.save()
    def __str__(self):
        return self.descriptions
