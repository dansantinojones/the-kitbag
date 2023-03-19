from django.shortcuts import render
from .models import Shirt

# Create your views here.


def all_shirts(request):
    """ A view to show all products, sorting and search queries """

    shirts = Shirt.objects.all()

    context = {
        'shirts': shirts,
    }

    return render(request, 'shirts/shirts.html', context)