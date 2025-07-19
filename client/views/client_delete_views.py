import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from django.http import Http404
from ..models import Client

logger = logging.getLogger(__name__)

class ClientDeleteView(APIView):
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        return super().get_permissions()
    
    def delete(self, request, pk):
        try:
            logger.info(f"Attempting to delete Client with id={pk}")
            client = get_object_or_404(Client, pk=pk)
            client.delete()
            logger.info(f"Client with id={pk} deleted successfully")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            logger.warning(f"Client with id={pk} not found")
            raise
        except Exception as e:
            logger.error(f"Error deleting Client with id={pk}: {e}", exc_info=True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
