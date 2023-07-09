from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from web_project import settings
from posts.views import (main_view,
                          products_view, 
                          categoria_view,
                          product_detail_view, 
                          product_create_view,
                          categories_create_view
                          )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('categoria/', categoria_view),
    path('products/<int:pk>/',product_detail_view),
    path('products/create/',product_create_view),
    path('categoria/categories/', categories_create_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
