from django.urls import path
from familia.views import familia

urlpatterns =[
    path('', familia, name = 'familia'),
]