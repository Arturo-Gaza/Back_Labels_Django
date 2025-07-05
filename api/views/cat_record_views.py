from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.services.cat_record_service import CatRecordService
from api.serializers.cat_record_serializer import CatRecordSerializer

class CatRecordList(APIView):
    def get(self, request):
        try:
            records = CatRecordService.list_records()
            serializer = CatRecordSerializer(records, many=True)
            return Response({
                "message": "Registros cargados correctamente",
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": f"Error al obtener registros: {str(e)}",
                "status": "error",
                "data": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Create your views here.

class CatRecordCreate(APIView):
    def post(self, request):
        serializer = CatRecordSerializer(data=request.data)
        if serializer.is_valid():
            record = CatRecordService.create_record(serializer.validated_data)
            return Response({
                "message": "Registro creado correctamente",
                "status": "success",
                "data": CatRecordSerializer(record).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Datos inválidos",
            "status": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
class CatRecordUpdate(APIView):
    def put(self, request, pk):
        try:
            instance = CatRecordService.get_record(pk)
            if not instance:
                return Response({
                    "message": "Record no encontrado",
                    "status": "error"
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = CatRecordSerializer(instance, data=request.data)
            if serializer.is_valid():
                updated = CatRecordService.update_record(pk, serializer.validated_data)
                return Response({
                    "message": "Record actualizado correctamente",
                    "status": "success",
                    "data": CatRecordSerializer(updated).data
                }, status=status.HTTP_200_OK)

            return Response({
                "message": "Datos inválidos",
                "status": "error",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": f"Error al actualizar: {str(e)}",
                "status": "error"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)