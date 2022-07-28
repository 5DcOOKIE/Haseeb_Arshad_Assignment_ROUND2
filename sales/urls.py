from django.urls import include
from django.urls import path
from rest_framework import routers

from sales.views.product import ProductViewSet
from sales.views.sale import SaleViewSet

router = routers.DefaultRouter()
router.register(r'sales', SaleViewSet, basename='sales')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
