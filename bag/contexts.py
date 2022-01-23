from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    free_delivery_threshold = 50
    standard_delivery_percentage = 0.1
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })


    if total < free_delivery_threshold:
        # Free delivery over £50
        delivery = total * Decimal(standard_delivery_percentage)
        # If less than £50, delivery charged at 10% of all items
        remaining_to_free_del = free_delivery_threshold - total
    else:
        delivery = 0
        remaining_to_free_del = 0
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'remaining_to_free_del': remaining_to_free_del,
        'grand_total': grand_total,
    }

    return context