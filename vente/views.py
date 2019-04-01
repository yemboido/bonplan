from django.shortcuts import render,redirect, get_object_or_404
from django.template.response import TemplateResponse
from vente.models import article
from .forms import formulaire_connexion,formulaire_inscription,PostForm
from django.utils import timezone
from django.contrib.auth import authenticate, login,logout
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse


def lire(request, id):
    posts = get_object_or_404(article, id=id)
    return render(request, 'vente/lire.html', {'posts':posts})
# Create your views here.
def articles(request):
    posts=article.objects.order_by('-date_publication')
    return render(request,'vente/index.html', {'posts': posts})


def Offre(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            article= form.save(commit=False)
            article.date_publication = timezone.now()
            article.save()
            return redirect('articles')
    form = PostForm()
    return render(request, 'vente/offre.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def connexion(request):
    error = False
    if request.method == "POST":
        form = formulaire_connexion(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"] # Nous  récupérons le nom d'utilisateur
            password = form.cleaned_data["password"] # … et le mot de passe
            user = authenticate(username=username,password=password) #Nous vérifions si les données sont correctes
            if user:# Si l'objet renvoyé n'est pas None
                login(request, user) # nous connectons l'utilisateur
            else: #sinon une erreur sera affichée
                error = True
    else:
        form = formulaire_connexion()
    return render(request, 'vente/connexion.html',locals())

def inscription(request):
    error=False
    if request.method == "POST":
        form=formulaire_inscription(request.POST)
        if form.is_valid():
            username = request.POST['username']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            u = User.objects.create_user(username, email, password, first_name=fname, last_name=lname)
            u.save()
            return HttpResponse("Registration complete! Please head over to the <a href='/articles/'>login page</a> to start using your website.")
    else:
        form=formulaire_inscription()
    return render(request, "vente/inscription.html",locals() )

def Demande(request):
    if request.method == "POST":
        form = formulaire_demande(request.POST)
        if form.is_valid():
            demande= form.save(commit=False)
            demande.save()
            return redirect('articles')

    else:
        form = formulaire_demande()
    return render(request, 'vente/demande.html', {'form': form})

def demande_objet(request):
    posts=demande.objects.order_by('-date_publication')
    return render(request,'vente/demande_objets.html', {'posts': posts})
