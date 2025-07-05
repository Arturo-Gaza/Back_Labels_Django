from api.models.cat_pais import CatPais

class CatPaisRepository:
    @staticmethod
    def get_all():
        return CatPais.objects.all()
    