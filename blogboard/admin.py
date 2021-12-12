from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):

    readonly_fields = ('username', 'date_of_entry')


admin.site.register(Blog, BlogAdmin)
