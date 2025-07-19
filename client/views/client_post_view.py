import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from ..serializers import ClientSerializer

logger = logging.getLogger(__name__)

class ClientPostView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()
    
    def post(self, request):
        try:
            logger.info("Received POST request to create a Client")
            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Client created successfully: {serializer.data}")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.warning(f"Client creation validation failed: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error during client creation: {e}", exc_info=True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
