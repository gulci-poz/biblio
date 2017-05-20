from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from shelf.models import BookItem


class Rental(models.Model):
    who = models.ForeignKey(User)
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{what}, rented by {who} at {when}" \
            .format(what=self.what, who=self.who, when=self.when)
