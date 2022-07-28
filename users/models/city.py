from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return f"{self.name}"
