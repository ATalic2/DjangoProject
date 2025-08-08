import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import MerchantSerializer

logger = logging.getLogger(__name__)

class MerchantPostView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()
    
    def post(self, request: Request) -> Response:
        try:
            serializer = MerchantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Merchant created: {serializer.data}")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning(f"Merchant creation validation failed: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error creating merchant: {e}", exc_info=True)
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
