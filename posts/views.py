from django.shortcuts import render
from posts.models import Product, Icon



def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')
    
def products_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        context_data = {
            'product': product
        }
        return render(request, 'products/products.html', context=context_data)
    
def categoria_view(request):
    if request.method == 'GET':
        icons = Icon.objects.all()
        context_data = {
            'icons': icons
        }
        return render(request, 'products/categoris.html', context=context_data)
