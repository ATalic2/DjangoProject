from django.urls import path
from merchant.views import MerchantListView, MerchantPostView, MerchantPatchView, MerchantDeleteView

urlpatterns = [
    path('list/', MerchantListView.as_view(), name='merchant-list'),
    path('post/', MerchantPostView.as_view(), name='merchant-post'),
    path('patch/', MerchantPatchView.as_view(), name='merchant-patch'),
    path('delete/<int:pk>/', MerchantDeleteView.as_view(), name='merchant-delete'),
]
