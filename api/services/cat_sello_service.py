# api/services/sello_service.py

from api.repositories.cat_sello_repository import SelloRepository

class SelloService:
    @staticmethod
    def list_sellos():
        return SelloRepository.get_sellos()
    
    @staticmethod
    def create_sello(data):
        return SelloRepository.create_sello(data)
