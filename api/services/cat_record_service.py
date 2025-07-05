from api.repositories.cat_record_repository import CatRecordRepository

#Service para enlistar los datos de una tabla
class CatRecordService():
    @staticmethod
    def list_records():
        return CatRecordRepository.get_all()

#Service para traer un datos por su id    
    @staticmethod
    def get_record(pk):
        return CatRecordRepository.get_record_by_id(pk)

#Service para crear un registro en la tabla   
    @staticmethod
    def create_record(data):
        return CatRecordRepository.create_record(data)

#Service para actualizar un dato en la tabla   
    @staticmethod
    def update_record(pk, data):
        record = CatRecordRepository.get_record_by_id(pk)
        if not record:
            raise Exception("Registro no encontrado")
        for key, value in data.items():
            setattr(record, key, value)
        record.save()
        return record
    
