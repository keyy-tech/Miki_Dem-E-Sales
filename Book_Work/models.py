from django.db import models


# Create your models here.

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_info = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10 ,decimal_places=2)
    product_stock = models.IntegerField()

    def __str__(self):
        return self.product_name


class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add=True)
    sale_quantity = models.IntegerField()
    sale_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.sale_id
