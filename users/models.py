from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

# ustawienia można dać w zmiennej LOGGING w settings.py
logger = logging.getLogger('django')


class BiblioUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, default='')

    class Meta:
        # to uprawnienie powinno się znajdować w aplikacji rental
        # kontekst wypożyczania jest związany z aplikacją rental
        permissions = (
            ('can_rent', 'Can rent a book'),
        )

    # sposób 1 dodanie uprawnienia użytkownikowi
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


# sposób 2 dodanie uprawnienia użytkownikowi
# nie da się efektywnie odebrać uprawnienia
# trzeba odpiąć sygnał i podpiąć z powrotem
# (udało się)
# sygnał musi się znajdować w miejscu, które będzie wykonane przez pythona
# modele są wykonywane na starcie
@receiver(post_save, sender=BiblioUser)
def add_rent_permission(sender, *args, **kwargs):
    user = kwargs.get('instance')
    try:
        p = Permission.objects.get(codename='can_rent')
        user.user_permissions.add(p)
        logger.info('Dodano uprawnienia')
    except Exception as e:
        logger.error('Wystąpił błąd w nadawaniu uprawnień: %s' % e)
