from django.shortcuts import render, redirect, reverse


def view_bag(request):
    """ a view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ a view that allows user to add a specified quantity of a product """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    length = None
    if 'rope_length' in request.POST:
        length = request.POST['rope_length']
    bag = request.session.get('bag', {})

    if length:
        if item_id in list(bag.keys()):
            if length in bag[item_id]['rope_by_length'].keys():
                bag[item_id]['rope_by_length'][length] += quantity
            else:
                bag[item_id]['rope_by_length'][length] = quantity
        else:
            bag[item_id] = {'rope_by_length': {length: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ adjust the quantity of specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    length = None
    if 'rope_length' in request.POST:
        length = request.POST['rope_length']
    bag = request.session.get('bag', {})

    if length:
        if quantity > 0:
            bag[item_id]['rope_by_length'][length] = quantity
        else:
            del bag[item_id]['rope_by_length'][length]
            if not bag[item_id]['rope_by_length']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
