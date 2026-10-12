from django.shortcuts import render, get_object_or_404
from .models import Category,Products
from django.db.models import Count
# Create your views here.
def category_list(request):
    categories = Category.objects.annotate(
        product_count=Count("products")
    ).filter(product_count__gt=0)

    products = Products.objects.filter(
        is_available=True
    ).order_by("price")

    return render(request, "products/category_list.html", {
        "categories": categories,
        "products": products
    })

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, "products/category_detail.html", {
        "category": category,
        "products": products
    })

def products_on_sale(request):
    products = Products.objects.filter(is_on_sale=True)

    return render(request, "products/products_on_sale.html", {
        "products": products
    })

def product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    return render(request, "products/product_detail.html", {
        "product": product
    })