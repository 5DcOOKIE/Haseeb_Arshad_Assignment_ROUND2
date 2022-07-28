from django.db.models import Avg, Max
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sales.models.sale import Sale
from sales.serializers.sale import SaleSerializer


# ViewSets define the view behavior.
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SalesReportViewSet(viewsets.ViewSet):
    # authentication_classes = [IsAuthenticated]

    @property
    def get_queryset(self):
        return Sale.objects.all()

    def list(self, request):
        # "average_sales_for_current_user":
        # "average_sale_all_user":
        # "highest_revenue_sale_for_current_user": {
        #     "sale_id": 80,
        #     "revenue": 1.25
        # },
        # "product_highest_revenue_for_current_user": {
        #     "product_name": "Tape dispenser",
        #     "price": 20
        # },
        # "product_highest_sales_number_for_current_user": {
        #     "product_name": "Tape dispenser",
        #     "price": 432
        # }
        queryset = self.get_queryset
        response = {}

        # average_sales_for_current_userprice__avg
        average_sales_for_current_user = queryset.filter(user_id=request.user.id).aggregate(Avg('revenue'))[
            'revenue__avg']
        if average_sales_for_current_user is None:
            average_sales_for_current_user = 0
        response['average_sales_for_current_user'] = average_sales_for_current_user

        # average_sale_all_user
        average_sale_all_user = queryset.aggregate(Avg('revenue'))['revenue__avg']
        if average_sale_all_user is None:
            average_sale_all_user = 0
        response['average_sale_all_user'] = average_sale_all_user

        # highest_revenue_sale_for_current_user
        highest_revenue_sale_for_current_user = queryset.filter(user_id=request.user.id).aggregate(Max('revenue'))[
            'revenue__max']
        if highest_revenue_sale_for_current_user is None:
            response['highest_revenue_sale_for_current_user'] = {
                'sale_id': 0,
                'revenue': 0
            }
        else:
            response['highest_revenue_sale_for_current_user'] = {
                'sale_id': queryset.filter(revenue=highest_revenue_sale_for_current_user).first().id,
                'revenue': highest_revenue_sale_for_current_user
            }

        # # product_highest_revenue_for_current_user
        # product_highest_revenue_for_current_user = queryset.filter(user_id=request.user.id).aggregate(Max('product__sale__revenue'))['product__sale__revenue__max']
        # if product_highest_revenue_for_current_user is None:
        #     response['product_highest_revenue_for_current_user'] = {
        #         'product_name': '',
        #         'price': 0
        #     }
        # else:
        #     response['product_highest_revenue_for_current_user'] = {
        #         'product_name': queryset.filter(product__price=product_highest_revenue_for_current_user).first().product.name,
        #         'price': product_highest_revenue_for_current_user
        #     }
        response['product_highest_revenue_for_current_user'] = {
            'product_name': '',
            'price': 0
        }

        # product_highest_sales_number_for_current_user
        # product_highest_sales_number_for_current_user = queryset.filter(user_id=request.user.id).aggregate(Max('product__sale__sales_number'))['product__sale__sales_number__max']
        # if product_highest_sales_number_for_current_user is None:
        #     response['product_highest_sales_number_for_current_user'] = {
        #         'product_name': '',
        #         'price': 0
        #     }
        # else:
        #     response['product_highest_sales_number_for_current_user'] = {
        #         'product_name': queryset.filter(product__sale__sales_number=product_highest_sales_number_for_current_user).first().product.name,
        #         'price': product_highest_sales_number_for_current_user
        #     }
        response['product_highest_sales_number_for_current_user'] = {
            'product_name': '',
            'price': 0
        }

        return Response(response)
