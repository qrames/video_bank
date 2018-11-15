# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Movie, MovieGenre, MovieRent
# Register your models here.
from parler.admin import TranslatableAdmin


class MovieAdmin(TranslatableAdmin):
    models = Movie


class MovieGenreAdmin(admin.ModelAdmin):
    models = MovieGenre


class MovieRentAdmin(admin.ModelAdmin):
    models = MovieRent




admin.site.register(Movie, MovieAdmin)

admin.site.register(MovieGenre, MovieGenreAdmin)

admin.site.register(MovieRent, MovieRentAdmin)
