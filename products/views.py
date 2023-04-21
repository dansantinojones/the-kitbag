from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Shirt, League, SellShirt
from .forms import ShirtForm, SellShirtForm


def all_shirts(request):
    """ A view to show all products, sorting and search queries """

    shirts = Shirt.objects.all()
    query = None
    leagues = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                shirts = shirts.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            shirts = shirts.order_by(sortkey)


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

    current_sorting = f'{sort}_{direction}'

    context = {
        'shirts': shirts,
        'search_term': query,
        'current_leagues': leagues,
        'current_sorting': current_sorting,
    }

    return render(request, 'shirts/shirts.html', context)


def shirt_detail(request, shirt_id):
    """ A view to show shirt details such as name, description, price and image """

    shirt = get_object_or_404(Shirt, pk=shirt_id)

    context = {
        'shirt': shirt,
    }

    return render(request, 'shirts/shirt_detail.html', context)


@login_required
def add_shirt(request):
    """ Add a shirt to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ShirtForm(request.POST, request.FILES)
        if form.is_valid():
            shirt = form.save()
            messages.success(request, 'Successfully added shirt!')
            return redirect(reverse('shirt_detail', args=[shirt.id]))
        else:
            form = ShirtForm()

    form = ShirtForm()
    template = 'shirts/add_shirt.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def sell_shirt(request):
    """ Sell a shirt to the store """
    if request.method == 'POST':
        form = SellShirtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for the offer! We will be in contact soon.')
            return redirect(reverse('sell_shirt'))
        else:
            form = SellShirt()

    form = SellShirtForm()
    template = 'shirts/sell_shirt.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_shirt(request, shirt_id):
    """ Edit a shirt in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    shirt = get_object_or_404(Shirt, pk=shirt_id)
    if request.method == 'POST':
        form = ShirtForm(request.POST, request.FILES, instance=shirt)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated shirt!')
            return redirect(reverse('shirt_detail', args=[shirt.id]))
        else:
            messages.error(request, 'Failed to update shirt. Please ensure the form is valid.')
    else:
        form = ShirtForm(instance=shirt)
        messages.info(request, f'You are editing {shirt.name}')

    template = 'shirts/edit_shirt.html'
    context = {
        'form': form,
        'shirt': shirt,
    }

    return render(request, template, context)


@login_required
def delete_shirt(request, shirt_id):
    """ Delete a shirt from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    shirt = get_object_or_404(Shirt, pk=shirt_id)
    shirt.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('shirts'))