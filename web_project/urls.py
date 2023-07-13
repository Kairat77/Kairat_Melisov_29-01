from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from web_project import settings

from django.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from posts.views import ProductAPIView
from posts.views import (main_view,
                          products_view, 
                          categoria_view,
                          product_detail_view, 
                          product_create_view,
                          categories_create_view
                          )


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for your project",
    ),
    public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', main_view),
    path('products/', products_view),
    path('categoria/', categoria_view),
    path('products/<int:pk>/',product_detail_view),
    path('products/create/',product_create_view),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('categoria/categories/', categories_create_view),
    path('api/v1/productlist/', ProductAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
