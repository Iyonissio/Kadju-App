from django.shortcuts import render
from apps.product.models import Product
from .models import Destaque

def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    return render(request, 'core/frontpage.html', {'newest_products': newest_products})

def destaque(request):
    novos_destaques = Destaque.objects.all()[0:8]
    return render(request, 'core/frontpage.html', {'novos_destaques': novos_destaques})

def contact(request):
    return render(request, 'core/contact.html')