from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.services.cat_pais_service import CatPaisService
from api.serializers.cat_pais_serializer import CatPaisSerializer

class PaisListView(APIView):
    def get(self, request):
        try:
            paises = CatPaisService.list_pais()
            serializer = CatPaisSerializer(paises, many=True)
            return Response({
                "message": "Países cargados correctamente",
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": f"Error al obtener países: {str(e)}",
                "status": "error",
                "data": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





