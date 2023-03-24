from django.contrib import admin
from .models import Bb
from .models import Rubric


class AdminBb(admin.ModelAdmin):
    list_display = ('title', 'text', 'price', 'rubric', 'published')
    list_display_links = ('title', 'text')
    search_fields = ('title', 'text')


admin.site.register(Bb, AdminBb)
admin.site.register(Rubric)
