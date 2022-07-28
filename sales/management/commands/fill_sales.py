import csv
import os
import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from sales.models.product import Product
from sales.models.sale import Sale

User = get_user_model()


class Command(BaseCommand):
    help = 'Fills the Seller table with data'

    def handle(self, *args, **options):
        path = 'sales/management/files/sales.csv'
        file_exists = os.path.exists(path)
        if not file_exists:
            self.stdout.write(self.style.ERROR('Directory Not Found'))
            return None

        user_ids = list(User.objects.all().values_list('id', flat=True))
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    # assign sale to random user
                    sale = Sale(
                        date=row[0],
                        sales_number=row[1],
                        revenue=row[2],
                        product=Product.objects.get(name=row[3]),
                        user_id=User.objects.get(id=random.choice(user_ids)))
                    sale.save()
                    line_count += 1
            self.stdout.write(self.style.SUCCESS(f'Successfully imported {line_count} sales'))
