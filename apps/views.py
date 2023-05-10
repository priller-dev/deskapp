from django.shortcuts import render, get_object_or_404
from .models import Product

def index_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def detail_view(request, uid):
    product = get_object_or_404(Product, id=uid)
    context = {
        'product': product
    }
    return render(request, 'product-detail.html', context)