from django.db import models

class Ville(models.Model):
    nomv = models.CharField("Nom de la ville", max_length=50)
    histoire = models.CharField("Histoire", max_length=1000)

    def __str__(self):
        return self.nomv

class Metier(models.Model):
    nomm = models.CharField("Nom du métier", max_length=50)
    niveaum = models.CharField("Niveau requis", max_length=50)

    def __str__(self):
        return self.nomm

class Personnels(models.Model): 
    nom = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    gmail = models.EmailField(default='cedricnyacke@gmail.com')
    daten = models.DateField()
    niveaup = models.CharField(max_length=50)
    famille = models.CharField(max_length=100)
    residence = models.CharField(max_length=100, default='Inconnu')
    ville = models.ForeignKey('Ville', on_delete=models.CASCADE)
    metier = models.ManyToManyField('Metier')
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return self.nom

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

    image = models.ImageField(
        upload_to='actualites/images/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='actualites/videos/',
        blank=True,
        null=True
    )

    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre