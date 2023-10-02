
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:   #DEBUG rejim uchun maxsus jonpath
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
