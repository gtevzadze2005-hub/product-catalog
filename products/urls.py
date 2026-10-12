from django.urls import path
from . import views

urlpatterns = [
    path("",views.category_list,name = "category_list"),
     path('categories/<int:category_id>/',
             views.category_detail,
             name = "category_detail"),
    path(
    'on-sale/',
    views.products_on_sale,
    name='products_on_sale'
),
path(
    'product/<int:product_id>/',
    views.product_detail,
    name='product_detail'
)
]
