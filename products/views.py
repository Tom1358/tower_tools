from django.shortcuts import render
from .models import Product

def ringing_equipment(request):
    """ a view to return ringing equipment products """

    ringing_equipment = Product.objects.get(pk=1)

    context = {
        'ringing_equipment': ringing_equipment,
    }

    return render(request, 'products/ringing_equipment.html', context)
