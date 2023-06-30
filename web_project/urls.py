from web_project import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import main_view, products_view, categoria_view,product_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('categoria/', categoria_view),
    path('products/<int:pk>/', product_detail_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
