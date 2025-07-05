from api.repositories.cat_pais_repository import CatPaisRepository

class CatPaisService:
    @staticmethod
    def list_pais():
        return CatPaisRepository.get_all()