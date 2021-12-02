from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ReceiptViewSet, generate_pdf


router = DefaultRouter()
router.register("clients", ClientViewSet, basename="clients")
router.register("receipts", ReceiptViewSet, basename="receipts")

urlpatterns = [
    path('', include(router.urls)),
    path('receipts/<int:receipt_id>/generate_pdf', generate_pdf, name='generate_pdf'),
]
