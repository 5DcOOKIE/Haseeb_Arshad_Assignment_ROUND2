from rest_framework import viewsets

from sales.models.product import Product
from sales.serializers.product import ProductSerializer


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
