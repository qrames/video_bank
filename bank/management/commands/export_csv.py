from django.core.management.base import BaseCommand
import csv
from django.utils import translation
from bank.models import Movie, MovieGenre



class Command(BaseCommand):

    def handle(self, *args, **options):
        translation.activate('fr')

        with open('movies.csv', 'w') as mycsvfile:
            writer = csv.writer(mycsvfile)

            writer.writerow([
                            "id",
                            "director",
                            "actors",
                            "director",
                            "picture",
                            "length",
                            "release_date",
                            "rented",
                            "trailer_url",
                            "country",
                            "title",
                            "slug",
                            "synopsis",
            ])

            for movie in Movie.objects.all():

                writer.writerow([
                                movie.id,
                                movie.director,
                                movie.actors,
                                movie.director,
                                movie.picture,
                                movie.length,
                                movie.release_date,
                                movie.rented,
                                movie.trailer_url,
                                movie.country,
                                movie.title,
                                movie.slug,
                                movie.synopsis,
                ])

        with open('movies.csv', 'r') as mycsvfile:
            print mycsvfile.read()

        # return response
