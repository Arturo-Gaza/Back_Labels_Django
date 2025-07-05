from rest_framework import serializers
from api.models import CatSello

class SelloCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatSello
        fields = ['nombre_sello', 'descripcion_sello', 'label', 'id_record', 'id_pais']

    def validate_nombre_sello(self, value):
        if self.instance is None or self.instance.nombre_sello != value:
            if CatSello.objects.filter(nombre_sello__iexact=value).exists():
                raise serializers.ValidationError("Ya existe un sello con ese nombre.")
            return value