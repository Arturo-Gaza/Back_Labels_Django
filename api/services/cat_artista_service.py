from api.repositories.cat_artista_repository import CatArtistaRepository

class CatArtistaService():
    @staticmethod
    def list_artistas():
        return CatArtistaRepository.get_artistas()
    @staticmethod
    def create_artista(data):
        return CatArtistaRepository.create_artista(data)