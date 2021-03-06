# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.conf import settings

from django.shortcuts import render, reverse

#CRUD  C(Create) R(List Detail) U(Update) D(Delete)
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from parler.views import TranslatableSlugMixin, TranslatableCreateView

from models import Movie, Customer, MovieRent
# Create your views here.

class AddMovie(TranslatableCreateView):
    model = Movie
    fields = "__all__"

    def get_success_url(self):
        return reverse("detail-movie", args=[self.object.slug])


class DetailMovie(TranslatableSlugMixin, DetailView):
    model = Movie
    

class ListMovies(ListView):
    model = Movie


class ListRentedMovies(ListView):
    model = Movie
    template_name = "bank/admin_movie_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ListRentedMovies, self).get_context_data(*args, **kwargs)
    #     for movie in context['movie_list'] :
    #         if movie.rented :
    #             movie_rent = MovieRent.objects.get(movie=movie)
    #             print "[%s loue le filme : %s]"  %(movie_rent.customer.user, movie_rent.movie.title)
    #
    #     return context
    #
    def get_queryset(self):
        rented = self.request.GET.get('rented', None)
        print "QUERY=", rented

        if rented != None:

            return Movie.objects.filter(Q(rented=True))

        else:
            return Movie.objects.all()


class UpdateMovie(TranslatableSlugMixin, UpdateView):
    model = Movie
    fields = "__all__"
    def get_success_url(self):
        return reverse("detail-movie", args=[self.object.slug])


class DeleteMovie(TranslatableSlugMixin, DeleteView):
    model = Movie
    success_url  = "movies"


class CreateCustomerViews(CreateView):
    model = Customer
    fields = "__all__"


class CreateMovieRentViews(CreateView):
    model = MovieRent
    fields = "__all__"
