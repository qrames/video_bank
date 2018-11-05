# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#CRUD  C(Create) R(List Detail) U(Update) D(Delete)
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from models import Movie
# Create your views here.

class AddMovie(CreateView):
    model = Movie
    fields = "__all__"

class DetailMovie(DetailView):
    model = Movie


class ListMovies(ListView):
    model = Movie


class UpdateMovie(CreateView):
    model = Movie


class DeleteMovie(DeleteView):
    model = Movie
