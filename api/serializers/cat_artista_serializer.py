from rest_framework import serializers
from api.models import CatArtistas

class ArtistaSerializar(serializers.ModelSerializer):
    class Meta:
        model = CatArtistas
        fields = ['id_artista', 'nombre_artista', 'id_pais']
        read_only_fields = ['id_artista']