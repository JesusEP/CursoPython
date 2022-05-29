from django.shortcuts import render
from familia.models import Familia

def familia(request):
    nuevo_familiar1 = Familia.objects.create(
        name = 'Robert Parr',
        alias = 'Mr. Increible',
        age = 40,
        born = '1882-02-24',
        kinship = 'Padre',
        power = 'Superfuerza')
    nuevo_familiar2 = Familia.objects.create(
        name = 'Helen Parr',
        alias = 'Elastigirl',
        age = 38,
        born = '1884-04-17',
        kinship = 'Madre',
        power = 'Elasticidad extrema')
    nuevo_familiar3 = Familia.objects.create(
        name = 'Violeta Parr',
        alias = 'Violeta',
        age = 14,
        born = '2009-11-16',
        kinship = 'Hija mayor',
        power = 'Invisibilidad, campos de fuerza')
    nuevo_familiar4 = Familia.objects.create(
        name = 'Dashiell Robert Parr',
        alias = 'Dash',
        age = 10,
        born = '2012-04-20',
        kinship = 'Hijo del medio',
        power = 'Super velocidad')
    nuevo_familiar5 = Familia.objects.create(
        name = 'Jack-Jack Parr',
        alias = 'Jack-Jack',
        age = 1,
        born = '2021-05-10',
        kinship = 'Hijo menor',
        power = 'Multipoderes (fuego, rayos laser, etc)')
    context = {'nuevo_familiar1':nuevo_familiar1, 'nuevo_familiar2':nuevo_familiar2,'nuevo_familiar3':nuevo_familiar3,'nuevo_familiar4':nuevo_familiar4,'nuevo_familiar5':nuevo_familiar5}
    return render(request, 'familia.html', context=context)
