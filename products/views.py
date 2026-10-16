from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Products
from django.db.models import Count
from products.forms import ProductField, ProductUpdateForm
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
def add_product(request):
    if request.method == 'POST':
        form = ProductField(request.POST)
        if form.is_valid():
            form.save()
        return redirect('category_list')
    else:
        form = ProductField()

    return render(request, "products/add_product.html", context = {"form": form})

def update_product(request, product_pk):
    product = get_object_or_404(Products, pk = product_pk)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance= product)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ProductUpdateForm(instance=product)
    return render(request,'products/update_product.html',context={"form":form,"product": product})

def delete_product(request , product_pk):
    product = get_object_or_404(Products, pk = product_pk)

    if request.method == 'POST':
        product.delete()

    return redirect('category_list')

def index(request):
    categories = Category.objects.annotate(num_products = Count('products'))
    return render(request, 'index.html', context={'categories': categories})