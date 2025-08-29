from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from account.permission import IsManagerOrAdmin, IsWaiter, IsCashier
from products.models import Item
from orders.models import Order, Payment
from products.serializers import ItemSerializer
from orders.serializers import OrderSerializer, PaymentSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, IsManagerOrAdmin]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsWaiter]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsCashier]


