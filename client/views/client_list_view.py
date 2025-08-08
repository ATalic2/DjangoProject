import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import Client
from ..serializers import ClientSerializer

logger = logging.getLogger(__name__)

class ClientListView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return super().get_permissions()
    
    def get(self, request: Request) -> Response:
        try:
            logger.info("Received GET request for Client list")
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            logger.info(f"Returning {len(serializer.data)} clients")
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error fetching Client list: {e}", exc_info=True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
