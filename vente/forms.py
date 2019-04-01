from django import forms
from django.contrib.auth.models import User

from .models import article

class PostForm(forms.ModelForm):
    photo1=forms.ImageField(required=False)
    photo2=forms.ImageField(required=False)
    photo3=forms.ImageField(required=False)
    photo4=forms.ImageField(required=False)
    class Meta:
        model = article
        fields = ('localite','categories','type','descriptions','prix','Numeros','photo1','photo2','photo3','photo4')
        required = ('localite','categories','type','descriptions','prix','Numeros')
        

class formulaire_connexion(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

class formulaire_inscription(forms.Form):
      username=forms.CharField(label="Username",max_length=30)
      first_name=forms.CharField(label="First Name",max_length=30)
      last_name=forms.CharField(label="Last Name")
      email=forms.CharField(label="Email Address")
      password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)
