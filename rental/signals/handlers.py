from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import BiblioUser

import logging

# ustawienia są w zmiennej LOGGING w settings.py
logger = logging.getLogger('django')


# sposób 2 dodania uprawnienia użytkownikowi - sygnał
@receiver(post_save, sender=BiblioUser)
def add_rent_permission(sender, *args, **kwargs):
    user = kwargs.get('instance')
    try:
        p = Permission.objects.get(codename='can_rent')
        user.user_permissions.add(p)
        logger.info('Dodano uprawnienia')
    except Exception as e:
        logger.error('Wystąpił błąd w nadawaniu uprawnień: %s' % e)
