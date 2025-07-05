# api/services/sello_service.py

from api.repositories.cat_sello_repository import SelloRepository

class SelloService:
    @staticmethod
    def list_sellos():
        return SelloRepository.get_sellos()
    
#Service para traer un datos por su id    
    @staticmethod
    def get_sello(pk):
        return SelloRepository.get_sello_by_id(pk)
    
    @staticmethod
    def create_sello(data):
        return SelloRepository.create_sello(data)

#Service para actualizar un dato en la tabla   
    @staticmethod
    def update_sello(pk, data):
        record = SelloRepository.get_sello_by_id(pk)
        if not record:
            raise Exception("Registro no encontrado")
        for key, value in data.items():
            setattr(record, key, value)
        record.save()
        return record