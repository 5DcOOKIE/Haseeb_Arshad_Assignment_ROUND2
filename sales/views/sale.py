from rest_framework import viewsets

from sales.models.sale import Sale
from sales.serializers.sale import SaleSerializer


# ViewSets define the view behavior.
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
