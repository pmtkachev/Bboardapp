from django.contrib import admin
from .models import Bb


class AdminBb(admin.ModelAdmin):
    list_display = ('title', 'text', 'price', 'published')
    list_display_links = ('title', 'text')
    search_fields = ('title', 'text')


admin.site.register(Bb, AdminBb)
