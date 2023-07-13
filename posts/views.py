from django.shortcuts import render, redirect
from rest_framework import viewsets
from posts.models import Product, Icon
from posts.forms import ProductCreateForm, CategoryCreateForm
from rest_framework import generics
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductAPIView(APIView):#автоматически генерирует
    def get(self, request):  #отвечает за обработку get запросов
        w = Product.objects.all()
        return Response({'posts': ProductSerializer(w, many=True).data})
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self,request, *args, **kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response({"error":"Method Put not allowed"})
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error":"Object doesnot exists"})
        
        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})


# class ProductAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



def main_view(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")


def products_view(request):
    if request.method == "GET":
        product = Product.objects.all()
        context_data = {"product": product}
        return render(request, "products/products.html", context=context_data)


def categoria_view(request):
    if request.method == "GET":
        icons = Icon.objects.all()
        context_data = {"icons": icons}
        return render(request, "products/categoris.html", context=context_data)


def product_detail_view(request, pk):
    if request.method == "GET":
        try:
            post = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(request, "products/detail.html")
    context_data = {"post": post}

    return render(request, "products/detail.html", context=context_data)


def product_create_view(request):
    if request.method == "GET":
        context_data = {"form": ProductCreateForm}
        return render(request, "products/create.html", context=context_data)
    if request.method == "POST":
        data, file = request.POST, request.FILES
        form = ProductCreateForm(data, file)
        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get("image"),
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
            )
            return redirect("/products/")
        return render(request, "products/create.html", context={"form": form})


def categories_create_view(request):
    if request.method == "GET":
        form = CategoryCreateForm()
        context_data = {"form": form}
        return render(request, "products/categories.html", context=context_data)
    if request.method == "POST":
        form = CategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            icon = form.cleaned_data.get("icon")
            if icon:
                Icon.objects.create(icon=icon)
                return redirect("/categoria/")
            else:
                form.add_error("icon", "Please choose a file.")
        context_data = {"form": form}
        return render(request, "products/categories.html", context=context_data)

