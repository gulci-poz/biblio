from django.conf import settings
from django.db import models
# from django.db.models import Q
from django.utils.timezone import now

from shelf.models import BookItem


class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    # what = models.ForeignKey(BookItem,
    #                          limit_choices_to=Q(
    #                              rental__returned__isnull=False
    #                          ) | Q(
    #                              rental__isnull=True
    #                          ))
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{what}, rented by {who} at {when}" \
            .format(what=self.what, who=self.who, when=self.when)

    # sposób 1 dodania uprawnienia użytkownikowi
    # w przypadku domyślnego użytkownika django nie mamy dostępu do save
    # i musimy korzystać z sygnałów
    # def save(self, *args, **kwargs):
    #     # najpierw musimy zapisać użytkownika, ponieważ potrzebujemy id,
    #     # potem możemy nadać mu uprawnienia
    #     super(BiblioUser, self).save(*args, **kwargs)
    #     try:
    #         p = Permission.objects.get(codename='can_rent')
    #         self.user_permissions.add(p)
    #         logger.info('Dodano uprawnienia')
    #     except Exception as e:
    #         # Permission.DoesNotExist
    #         # inny wyjątek w razie większej liczby obiektów
    #         logger.error('Wystąpił błąd w nadawaniu uprawnień: %s' % e)
    #         # -> testy

    class Meta:
        # kontekst wypożyczania jest związany z aplikacją rental
        permissions = (
            ('can_rent', 'Can rent a book'),
        )
