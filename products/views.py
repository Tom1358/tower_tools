from django.shortcuts import render, get_object_or_404
from .models import Product

def ringing_equipment(request):
    """ a view to return ringing equipment products """

    ringing_equipment = Product.objects.filter(category=1)

    context = {
        'ringing_equipment': ringing_equipment,
    }

    return render(request, 'products/ringing_equipment.html', context)


def merchandise(request):
    """ a view to return merchandise products """

    merchandise = Product.objects.filter(category=2)

    context = {
        'merchandise': merchandise,
    }

    return render(request, 'products/merchandise.html', context)


def learning_tools(request):
    """ a view to return learning tools products """

    learning_tools = Product.objects.filter(category=3)

    context = {
        'learning_tools': learning_tools,
    }

    return render(request, 'products/learning_tools.html', context)


def product_detail(request, product_id):
    """ a view to show the details of products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
