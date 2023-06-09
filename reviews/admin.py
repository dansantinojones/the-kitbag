from django.contrib import admin
from .models import Review


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'created_on',
        'rating',
        'body',
    )

    ordering = ('created_on',)


admin.site.register(Review, ReviewsAdmin)
