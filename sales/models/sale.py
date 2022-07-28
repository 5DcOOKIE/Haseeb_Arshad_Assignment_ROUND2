from django.db import models


class Sale(models.Model):
    date = models.DateField(null=True, blank=True)
    sales_number = models.IntegerField(default=0)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    products = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'sale'
        verbose_name_plural = 'sales'

    def __str__(self):
        return f"{self.id}"
