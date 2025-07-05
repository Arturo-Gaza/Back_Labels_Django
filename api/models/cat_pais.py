from django.db import models

class CatPais(models.Model):
    id_pais = models.BigAutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=100)


    class Meta:
        db_table = 'cat_pais'  # Nombre exacto en la base de datos
        managed = False