from django.urls import include
from django.urls import path
from rest_framework import routers

from sales.views.product import ProductViewSet
from sales.views.sale import SaleViewSet
from sales.views.sale_report import SalesReportViewSet

router = routers.DefaultRouter()
router.register(r'sales', SaleViewSet, basename='sales_api')
router.register(r'products', ProductViewSet, basename='products_api')
router.register(r'sale_statistics', SalesReportViewSet, basename='sale_statistics_api')


urlpatterns = [
    path('', include(router.urls)),
]
