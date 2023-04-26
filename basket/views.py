from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Shirt


def view_basket(request):
    """ A view that renders the basket content page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a spesific shirt to the basket """

    shirt = get_object_or_404(Shirt, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += 1
    else:
        basket[item_id] = 1

    messages.success(request, f'Added {shirt.name} to your basket')
    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """Remove the item from the basket"""
    try:
        shirt = get_object_or_404(Shirt, pk=item_id)
        basket = request.session.get('basket', {})
            
        basket.pop(item_id)
        messages.success(request, f'Removed {shirt.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
