from django.contrib import admin

from .models import UrlShortener


class UrlShortenerAdmin(admin.ModelAdmin):
    list_display = ('create_date', 'click_counter', 'long_url', 'short_url')


admin.site.register(UrlShortener, UrlShortenerAdmin)
