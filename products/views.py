from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product
from .forms import ProductForm

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


@login_required
def add_product(request):
    """ Add a product to the site """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit a product on the site """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from site """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('home'))