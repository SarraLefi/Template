from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Products(TemplateView):
    template_name = "ecommerce/ecommerce-products.html"
class ProductsDetail(TemplateView):
    template_name = "ecommerce/ecommerce-product-detail.html"
class ProductsOrder(TemplateView):
    template_name = "ecommerce/ecommerce-orders.html"
class ProductsCustomers(TemplateView):
    template_name = "ecommerce/ecommerce-customers.html"
class ProductsCart(TemplateView):
    template_name = "ecommerce/ecommerce-cart.html"
class ProductsCheckout(TemplateView):
    template_name = "ecommerce/ecommerce-checkout.html"
class ProductsShops(TemplateView):
    template_name = "ecommerce/ecommerce-shops.html"
class ProductsAddProduct(TemplateView):
    template_name = "ecommerce/ecommerce-add-product.html"
