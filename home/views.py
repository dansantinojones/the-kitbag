from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about_us(request):
    """ A view to return the about us page """

    return render(request, 'home/about_us.html')


def contact_us(request):
    """ A view to return the contact us page """

    return render(request, 'home/contact_us.html')


def faqs(request):
    """ A view to return the FAQ's page """

    return render(request, 'home/faqs.html')


def returns(request):
    """ A view to return the returns policy page """

    return render(request, 'home/returns.html')


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')


def newsletter_signup(request):
    """ Sign up to newsletter """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            # message.success(request, 'Thanks for signing up to our weekly newsletter!')
            return redirect(reverse('home'))
        else:
            form = NewsletterForm()

    form = NewsletterForm()
    context = {
        'form': form,
    }
    return redirect(reverse('home'))
