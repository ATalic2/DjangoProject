import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from django.http import Http404
from ..models import Merchant
from ..serializers import MerchantSerializer

logger = logging.getLogger(__name__)

class MerchantPatchView(APIView):
    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsAdminUser()]
        return super().get_permissions()
    
    def patch(self, request):
        merchant_id = request.data.get('id')
        if not merchant_id:
            return Response(
                {"error": "Merchant ID is required in the request body."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            merchant = get_object_or_404(Merchant, pk=merchant_id)
            serializer = MerchantSerializer(merchant, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Merchant {merchant_id} updated successfully")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.warning(f"Invalid data for Merchant {merchant_id}: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            logger.warning(f"Merchant with id {merchant_id} not found")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while updating Merchant {merchant_id}: {e}", exc_info=True)
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )