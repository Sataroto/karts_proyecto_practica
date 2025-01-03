from django.db import models

# Create your models here.

class CategoriaProd(models.Model):

    nombre = models.CharField(max_length=50)
    created = models.DateTimeField( auto_now_add= True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField( max_length=50)
    

