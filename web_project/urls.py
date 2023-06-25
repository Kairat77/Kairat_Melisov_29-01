from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import main_view, products_view, categoria_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('categoria/', categoria_view)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
