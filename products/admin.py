from django.contrib import admin
from .models import Shirt, League, SellShirt


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


class SellShirtAdmin(admin.ModelAdmin):
    list_display = (
        'team_name',
        'home_away_third',
        'league',
        'year',
        'size',
        'condition',
        'additional_info',
        'image_front',
        'image_back',
        'full_name',
        'email',
        'phone_number',
        )


admin.site.register(Shirt, ShirtAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(SellShirt, SellShirtAdmin)
