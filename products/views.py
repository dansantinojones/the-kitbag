from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages 
from django.db.models import Q
from .models import Shirt, League

# Create your views here.


def all_shirts(request):
    """ A view to show all products, sorting and search queries """

    shirts = Shirt.objects.all()
    query = None
    leagues = None

    if request.GET:
        if 'league' in request.GET:
            leagues = request.GET['league'].split(',')
            shirts = shirts.filter(league__name__in=leagues)
            leagues = League.objects.filter(name__in=leagues)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('shirts'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            shirts = shirts.filter(queries)

    context = {
        'shirts': shirts,
        'search_term': query,
        'current_leagues': leagues,
    }

    return render(request, 'shirts/shirts.html', context)


def shirt_detail(request, shirt_id):
    """ A view to show shirt details such as name, description, price and image """

    shirt = get_object_or_404(Shirt, pk=shirt_id)

    context = {
        'shirt': shirt,
    }

    return render(request, 'shirts/shirt_detail.html', context)