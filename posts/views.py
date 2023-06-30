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
    
def product_detail_view(request, pk):
    if request.method == 'GET':
        try:
            post = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(request, 'products/detail.html')
    context_data = {
        'post': post
    }
    return render(request, 'products/detail.html', context=context_data)
