from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < 50:
        # Free delivery over £50
        delivery = total * Decimal(0.1)
        # If less than £50, delivery charged at 10% of all items
        remaining_to_free_del = 50 - total
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