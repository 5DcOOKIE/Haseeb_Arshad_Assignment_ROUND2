from django.urls import include
from django.urls import path
from rest_framework import routers

from sales.views.product import ProductViewSet
from sales.views.sale import SaleViewSet, SalesReportViewSet

router = routers.DefaultRouter()
router.register(r'sales', SaleViewSet, basename='sales')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'sale_statistics', SalesReportViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
]
