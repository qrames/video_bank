# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.conf import settings

from django.shortcuts import render, reverse

#CRUD  C(Create) R(List Detail) U(Update) D(Delete)
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from models import Movie
# Create your views here.

class AddMovie(CreateView):
    model = Movie
    fields = "__all__"

    def get_success_url(self):
        return reverse("detail-movie", args=[self.object.slug])


class DetailMovie(DetailView):
    model = Movie


class ListMovies(ListView):
    model = Movie


class ListRentedMovies(ListView):
    model = Movie
    template_name = "bank/admin_movie_list.html"

    def get_queryset(self):
        rented = self.request.GET.get('rented', None)
        print "QUERY=", rented

        if rented != None:

            return Movie.objects.filter(Q(rented=False))

        else:
            return Movie.objects.all()


class UpdateMovie(UpdateView):
    model = Movie
    fields = "__all__"
    def get_success_url(self):
        return reverse("detail-movie", args=[self.object.slug])


class DeleteMovie(DeleteView):
    model = Movie
    success_url  = "movies"
