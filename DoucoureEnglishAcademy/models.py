from django.db import models

# Create your models here.

class Cours(models.Model):
    titre = models.CharField(max_length=200)        # Le nom du cours
    description = models.TextField()                # Description du cours
    date_debut = models.DateField()                 # Date de début
    date_fin = models.DateField()                   # Date de fin
    duree_heures = models.IntegerField()           # Durée en heures
    enseignant = models.CharField(max_length=100)   # Nom de l'enseignant
    niveau = models.CharField(max_length=50)        # Niveau (débutant, intermédiaire, avancé)
    prix = models.DecimalField(max_digits=8, decimal_places=2)  # Prix du cours

    

    class Meta:
        verbose_name = ("Cour")
        verbose_name_plural = ("Cours")

    def __str__(self):
        return self.titre

