from rest_framework import serializers
from api.models import CatPais

class CatPaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatPais
        fields = ['id_pais','nombre_pais']
        read_only_fields = ['id_pais']