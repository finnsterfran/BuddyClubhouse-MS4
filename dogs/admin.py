from django.contrib import admin
from .models import Dog, Breed, Job


class DogAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'breed',
        'resided_since',
        'age',
        'gender',
        'image',
        'story',
    )
    ordering = ('name',)


class BreedAdmin(admin.ModelAdmin):

    list_display = (
        'breed_name',
    )


class JobAdmin(admin.ModelAdmin):

    list_display = (
        'title',
    )


admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Job, JobAdmin)
