from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = "categories"
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    is_on_sale = models.BooleanField(default = False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True,  related_name="products")

    class Meta:
        db_table = "products"
    def __str__(self):
        return self.name