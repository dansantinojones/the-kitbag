from django.contrib import admin
from .models import Newsletter

# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'added_on',
    )

    ordering = ('added_on',)


admin.site.register(Newsletter, NewsletterAdmin)
