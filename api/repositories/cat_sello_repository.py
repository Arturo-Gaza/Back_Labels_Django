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


