from rest_framework import serializers
from api.models.cat_record import CatRecord

class CatRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatRecord
        fields = ['id_record', 'nombre_record', 'descripcion_record', 'img_record']
        read_only_fields = ['id_record']
        
    def validate_nombre_record(self, value):
        if self.instance is None or self.instance.nombre_record != value:
            if CatRecord.objects.filter(nombre_record__iexact=value).exists():
                raise serializers.ValidationError("Ya existe un record con ese nombre.")
        return value