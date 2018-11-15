from django.core.management.base import BaseCommand

from bank.models import MovieRent
from django.utils.translation import ugettext_lazy as _

from datetime import datetime, timedelta
import pytz

from mail_templated import send_mail

from django.template.loader import render_to_string

class Command(BaseCommand):
    help = "Relancer un Client qui n'a pas rendu un film"

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        relance = {}
        for rent in MovieRent.objects.filter(return_date__isnull=True) :
            #movie not return
            if rent.checkout_date + timedelta(days=0) <= datetime.now(pytz.utc):
                #max return date exceed
                if relance.has_key(rent.customer):
                    relance[rent.customer] += (rent.movie,)
                else :
                    relance[rent.customer] = (rent.movie,)

                print "Mm/M : %s %s" %(rent.customer.user.first_name, rent.customer.user.last_name)

        for customer, movies in relance.items():
            print "Mm/M : %s %s %s" %(customer.user.first_name, customer.user.last_name, customer.user.email)

            from django.core.mail import send_mail

            # msg_plain = render_to_string('templates/bank/email/relance_client.txt', {'customer': customer, 'movies': movies})
            msg_html = render_to_string('bank/email/relance_client.html', {'customer': customer, 'movies': movies})

            send_mail(
                'RELANCE: video rent %s %s' %(customer.user.first_name, customer.user.last_name),
                # msg_plain,
                'quentinrames@gmail.com',
                [customer.user.email],
                html_message=msg_html,
            )
