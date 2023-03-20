from django.shortcuts import render, get_object_or_404
from .models import Shirt

# Create your views here.


def all_shirts(request):
    """ A view to show all products, sorting and search queries """

    shirts = Shirt.objects.all()

    context = {
        'shirts': shirts,
    }

    return render(request, 'shirts/shirts.html', context)


def shirt_detail(request, shirt_id):
    """ A view to show shirt details such as name, description, price and image """

    shirt = get_object_or_404(Shirt, pk=shirt_id)

    context = {
        'shirt': shirt,
    }

    return render(request, 'shirts/shirt_detail.html', context)