from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services.cat_artista_service import CatArtistaService
from api.serializers.cat_artista_serializer import ArtistaSerializar

class CatArtistaListView(APIView):
    def get(self, request):
        try:
            artistas = CatArtistaService.list_artistas()
            return Response({
                "message": "Artistas cargados correctamente",
                "status": "success",
                "data": artistas
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": f"Error al obtener artistas: {str(e)}",
                "status": "error",
                "data": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class CatArtistaCreate(APIView):
    def post(self, request):
        serializer = ArtistaSerializar(data=request.data)
        if serializer.is_valid():
            artista = CatArtistaService.create_artista(serializer.validated_data)
            return Response({
                "message": "Artista creado correctamente",
                "status" : "seccess",
                "data" : ArtistaSerializar(artista).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "Message": "Datos invalidos",
            "status": "error",
            "errors": serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)