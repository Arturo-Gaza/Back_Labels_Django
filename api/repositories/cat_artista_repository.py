from api.models.cat_artista import CatArtistas

class CatArtistaRepository:
    @staticmethod
    def get_artistas():
        return CatArtistas.objects.select_related('id_pais')\
            .values(
                'id_artista',
                'nombre_artista',
                'id_pais__nombre_pais'
            ).order_by('nombre_artista')
            
    @staticmethod
    def create_artista(data):
        return CatArtistas.objects.create(**data)