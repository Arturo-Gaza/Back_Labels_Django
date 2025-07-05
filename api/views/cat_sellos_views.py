from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.cat_sello_serializer import SelloCreateSerializer
from api.services.cat_sello_service import SelloService

class SelloListView(APIView):
    def get(self, request):
        try:
            sellos = SelloService.list_sellos()
            return Response({
                "message": "Sellos cargados correctamente",
                "status": "success",
                "data": sellos
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": f"Error al obtener sellos: {str(e)}",
                "status": "error",
                "data": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class CatSelloCreate(APIView):
    def post(self, request):
        serializer = SelloCreateSerializer(data=request.data)
        if serializer.is_valid():
            record = SelloService.create_sello(serializer.validated_data)
            return Response({
                "message": "Registro creado correctamente",
                "status": "success",
                "data": SelloCreateSerializer(record).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Datos inválidos",
            "status": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)