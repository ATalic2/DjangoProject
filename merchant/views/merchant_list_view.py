import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Merchant
from ..serializers import MerchantSerializer

logger = logging.getLogger(__name__)

class MerchantListView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return super().get_permissions()
    
    def get(self, request):
        try:
            logger.info("Fetching all merchants")
            merchants = Merchant.objects.all()
            serializer = MerchantSerializer(merchants, many=True)
            logger.info(f"Returned {len(merchants)} merchants")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error fetching merchants: {e}", exc_info=True)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
