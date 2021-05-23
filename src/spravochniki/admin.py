from django.contrib import admin
from . import models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Publisher, PublisherAdmin)