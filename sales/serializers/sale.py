from rest_framework import serializers

from sales.models.sale import Sale


# Sale Serializer
class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'date', 'sales_number', 'revenue', 'products', 'user_id',)
