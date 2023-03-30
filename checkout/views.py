from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PaymentForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty!")
        return redirect(reverse('shirts'))

    payment_form = PaymentForm()
    template = 'checkout/checkout.html'
    context = {
        'payment_form': payment_form,
    }

    return render(request, template, context)
