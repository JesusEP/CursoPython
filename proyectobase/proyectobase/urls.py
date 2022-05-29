from django.contrib import admin
from django.urls import path, include
from proyectobase.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', include('familia.urls')),
    path('', index, name = 'index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)