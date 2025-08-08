import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from ..models import Client
from ..serializers import ClientSerializer

logger = logging.getLogger(__name__)

class ClientPatchView(APIView):
    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsAdminUser()]
        return super().get_permissions()

    def patch(self, request: Request) -> Response:
        client_id = request.data.get('id')
        if not client_id:
            logger.warning("PATCH called without client id in request data")
            return Response({"error": "Client ID is required in the request body."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            client = get_object_or_404(Client, pk=client_id)
            logger.info(f"Patching client with id {client_id}")
            serializer = ClientSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Client {client_id} updated successfully")
                return Response(serializer.data)
            logger.warning(f"Validation errors for client {client_id}: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error patching client {client_id}: {e}", exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
