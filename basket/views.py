from django.shortcuts import render, redirect

# Create your views here.


def view_basket(request):
    """ A view that renders the basket content page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a spesific shirt to the basket """

    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += 1
    else:
        basket[item_id] = 1

    request.session['basket'] = basket
    return redirect(redirect_url)