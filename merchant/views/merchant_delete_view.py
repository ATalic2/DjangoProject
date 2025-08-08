import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from ..models import Merchant

logger = logging.getLogger(__name__)

class MerchantDeleteView(APIView):
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        return super().get_permissions()
    
    def delete(self, request: Request, pk: int) -> Response:
        try:
            logger.info(f"Attempting to delete Merchant with id={pk}")
            merchant = get_object_or_404(Merchant, pk=pk)
            merchant.delete()
            logger.info(f"Merchant with id={pk} deleted successfully")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            logger.warning(f"Merchant with id={pk} not found")
            raise
        except Exception as e:
            logger.error(f"Error deleting Merchant with id={pk}: {e}", exc_info=True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
