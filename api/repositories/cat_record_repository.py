from api.models.cat_record import CatRecord

#Metodo para solicitar todos los datos de una tabla
class CatRecordRepository:
    @staticmethod
    def get_all():
        return CatRecord.objects.all().order_by('nombre_record')
    
#Metodo para crear un registro a la base de datos
    @staticmethod
    def create_record(data):
        return CatRecord.objects.create(**data)

#Metodo para solicitar un registro por su id
    @staticmethod
    def get_record_by_id(pk):
        try:
            return CatRecord.objects.get(pk=pk)
        except CatRecord.DoesNotExist:
            return None