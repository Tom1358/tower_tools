from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

def view_bag(request):
    """ a view that renders the bag contents page """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ a view that allows user to add a specified quantity of a product """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ remove an item """

    bag = request.session.get('bag', {})

    bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
