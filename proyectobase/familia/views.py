from django.shortcuts import render
from familia.models import Familia

def familia(request):
    familiares = Familia.objects.all()
    context = {'familiares':familiares}
    return render(request, 'familia.html', context=context)
