from django.db import models

class CatArtistas(models.Model):
    id_artista = models.BigAutoField(primary_key=True)
    nombre_artista = models.CharField(max_length=100)
    id_pais = models.ForeignKey(
        'CatPais',
        on_delete=models.CASCADE,
        db_column='id_pais'
    )
    
    class Meta:
        db_table = 'cat_artistas'
        managed = True