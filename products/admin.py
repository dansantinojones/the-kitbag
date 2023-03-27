from django.contrib import admin
from .models import Shirt, League

# Register your models here.


class ShirtAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'league',
        'price',
        'size',
        'image',
    )

    ordering = ('sku',)


class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Shirt, ShirtAdmin)
admin.site.register(League, LeagueAdmin)