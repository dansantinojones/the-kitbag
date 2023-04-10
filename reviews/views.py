from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import PostReviewForm

# Create your views here.

def reviews(request):
    """ A view to return the reviews page """

    return render(request, 'reviews/reviews.html')


@login_required
def post_review(request):
    """ Post a review """
    if request.method == 'POST':
        form = PostReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for posting a review!')
            return redirect(reverse('reviews'))
        else:
            form = PostReviewForm()

    form = PostReviewForm()
    template = 'reviews/reviews.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
