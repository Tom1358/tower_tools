from django.shortcuts import render
from .models import Product

def ringing_equipment(request):
    """ a view to return ringing equipment products """

    ringing_equipment = Product.objects.get(category=1)

    context = {
        'ringing_equipment': ringing_equipment,
    }

    return render(request, 'products/ringing_equipment.html', context)


def merchandise(request):
    """ a view to return merchandise products """

    merchandise = Product.objects.get(category=2)

    context = {
        'merchandise': merchandise,
    }

    return render(request, 'products/merchandise.html', context)
