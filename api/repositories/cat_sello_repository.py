from api.models.cat_sello import CatSello

class SelloRepository:
    @staticmethod
    def get_sellos():
        return CatSello.objects.select_related('id_pais', 'id_record') \
            .values(
                'id_sello',
                'nombre_sello',
                'descripcion_sello',
                'label',
                'id_pais__nombre_pais',
                'id_record__nombre_record'
            ).order_by('nombre_sello')
            
    @staticmethod
    def create_sello(data):
        return CatSello.objects.create(**data)

#Metodo para solicitar un registro por su id
    @staticmethod
    def get_sello_by_id(pk):
        try:
            return CatSello.objects.get(pk=pk)
        except CatSello.DoesNotExist:
            return None

