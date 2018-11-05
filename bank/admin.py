# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Customer, Movie, MovieGenre, MovieRent
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    models = Customer


class MovieAdmin(admin.ModelAdmin):
    models = Movie


class MovieGenreAdmin(admin.ModelAdmin):
    models = MovieGenre


class MovieRentAdmin(admin.ModelAdmin):
    models = MovieRent


admin.site.unregister(Customer)
admin.site.register(Customer, CustomerAdmin)


admin.site.register(Movie, MovieAdmin)

admin.site.register(MovieGenre, MovieGenreAdmin)

admin.site.register(MovieRent, MovieRentAdmin)
