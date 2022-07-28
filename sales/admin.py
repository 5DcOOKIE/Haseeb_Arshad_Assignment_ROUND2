from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from sales.models.product import Product
from sales.models.sale import Sale


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Sale)
class SaleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'date', 'sales_number', 'revenue', 'products', 'user_id')
