from django.db import models

class CatSello(models.Model):
    id_sello = models.BigAutoField(primary_key=True)
    nombre_sello = models.CharField(max_length=100)
    descripcion_sello = models.CharField(max_length=500)
    id_pais = models.ForeignKey(
        'CatPais',
        on_delete=models.CASCADE,
        db_column='id_pais'  # Le dices que la columna se llama así, sin _id
    )
    id_record = models.ForeignKey(
        'CatRecord',
        on_delete=models.CASCADE,
        db_column='id_record'
    )
    label = models.TextField()  # <- Agrega este campo
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'cat_sellos'
        managed = False