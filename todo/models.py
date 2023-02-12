from django.db import models
from django.conf import settings

# Create your models here.
class Note(models.Model):
    titre = models.CharField(max_length=50, blank=True, null=True)
    
    creation_date = models.DateField(auto_now_add=True)
    
    update_date = models.DateField(auto_now=True)
    
    contenu = models.TextField(blank=True, null=True)
    
    is_public = models.BooleanField(null=True)
    
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    
    def extrait(self, length=25):
        
        if len(self.contenu) <= length:
            return self.contenu
        else:
            return self.contenu[0:length-1]  