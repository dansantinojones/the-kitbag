from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PurchaseForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty!")
        return redirect(reverse('shirts'))

    payment_form = PurchaseForm()
    template = 'checkout/checkout.html'
    context = {
        'purchase_form': payment_form,
        'stripe_public_key': 'pk_test_51MexdSJdBBjifI631AOGfNY5Hi919aG6uyn0VadqjAfDWgDJKhsg9EB0t8TLw3KIbdc1OnqVuOP2Ebr9k61KF0V400hnvoYDhL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
