import os
from django.shortcuts import render, redirect, reverse

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('home'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': os.environ.get('STRIPE_PUBLIC_KEY'),
    }

    return render(request, template, context)
