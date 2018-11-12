# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

from django.db import models

from userena.models import UserenaBaseProfile


# Create your models here.

class Customer(UserenaBaseProfile):
    user = models.OneToOneField(User,
                            unique=True,
                            verbose_name=_('user'),
                            related_name='customer')


class MovieGenre(models.Model):
    label = models.CharField(verbose_name=_('Genre'), max_length=100, null=False)
    slug = AutoSlugField(populate_from='label')

    def __unicode__(self):
        return self.label


class Movie(models.Model):
    actors = models.CharField(verbose_name=_('Acteurs'), max_length=200, null=True)
    country = models.CharField(verbose_name=_('Pays'), max_length=100, null=True)
    director = models.CharField(verbose_name=_('directeur'), max_length=100, null=False)
    title = models.CharField(verbose_name=_('titre'), max_length=200, null=False)

    picture = models.ImageField(verbose_name=_('Affiche du film'))

    length = models.TimeField(verbose_name=_('Durée'), auto_now=False, auto_now_add=False)

    release_date = models.DateField(auto_now=False, auto_now_add=False)
    rented = models.BooleanField(verbose_name=_('En Location'),)

    slug = AutoSlugField(populate_from='title')

    trailer_url = models.URLField(max_length=200, null=True, blank=True)
    synopsis = models.TextField(verbose_name=_('synopsis'), null=True)
    genre =  models.ManyToManyField(MovieGenre)

    def __unicode__(self):
        return '"%s" de : %s' % (self.title.upper(), self.director)


class MovieRent(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(verbose_name=_("Date de l'emprunt"), auto_now_add=True)
    return_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
