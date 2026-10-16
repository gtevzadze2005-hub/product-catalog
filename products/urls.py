from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),

    
    path("products/", views.category_list, name="category_list"),

    # Categories
    path(
        "categories/<int:category_id>/",
        views.category_detail,
        name="category_detail",
    ),

    # Products on sale
    path(
        "on-sale/",
        views.products_on_sale,
        name="products_on_sale",
    ),

    # Product details
    path(
        "product/<int:product_id>/",
        views.product_detail,
        name="product_detail",
    ),

    # Add a product
    path("add-product/", views.add_product, name="add_product"),

    # Update a product
    path(
        "update_product/<int:product_pk>/",
        views.update_product,
        name="update_product",
    ),

    # Delete a product
    path(
        "delete_product/<int:product_pk>/",
        views.delete_product,
        name="delete_product",
    ),
]
