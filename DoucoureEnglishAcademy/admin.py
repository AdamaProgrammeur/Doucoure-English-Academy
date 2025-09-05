from django.contrib import admin
from .models import Cours

# Register your models here.

# admin.py
from django.contrib import admin
from .models import Cours

class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'niveau', 'date_debut', 'date_fin', 'prix', 'enseignant')  # colonnes affichées
    search_fields = ('titre', 'niveau')                           # barre de recherche
    list_filter = ('niveau', 'date_debut')                        # filtres à droite

admin.site.register(Cours, CoursAdmin)

