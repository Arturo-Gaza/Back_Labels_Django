from django.db import models

class CatRecord(models.Model):
    id_record = models.BigAutoField(primary_key=True)
    nombre_record = models.CharField(max_length=255)
    descripcion_record = models.CharField(max_length=500)
    img_record = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'cat_records'
        managed = False  # Django no gestionará la tabla ni migraciones