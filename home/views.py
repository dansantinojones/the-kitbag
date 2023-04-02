from django.shortcuts import render

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