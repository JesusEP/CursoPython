from django.contrib import admin
from django.urls import path, include
from proyectobase.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', include('familia.urls')),
    path('', index, name = 'index')
]
