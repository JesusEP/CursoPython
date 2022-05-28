from django.shortcuts import render
from familia.models import Familia

def familia(request):
    nuevo_familiar = Familia.objects.create(
            name = 'Jack-Jack Parr',
            age = 1,
            kinship = 'Hijo menor',
            power = 'Multipoderes'
            )
    context = {'nuevo_familiar':nuevo_familiar}
    return render(request, 'familia.html', context=context)
