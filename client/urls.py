from django.urls import path
from client.views import ClientListView, ClientPostView, ClientPatchView, ClientDeleteView

urlpatterns = [
    path('list/', ClientListView.as_view(), name='client-list'),
    path('post/', ClientPostView.as_view(), name='client-post'),
    path('patch/', ClientPatchView.as_view(), name='client-patch'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),
]
