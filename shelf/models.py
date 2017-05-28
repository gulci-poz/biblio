from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    # pierwszy atrybut to verbose_name (nie w polach relacyjnych)
    first_name = models.CharField(_('first_name'), max_length=20)
    last_name = models.CharField(_('last_name'), max_length=50)

    def __str__(self):
        return _("{first_name} {last_name}") \
            .format(first_name=self.first_name, last_name=self.last_name)

    class Meta:
        # sortowanie danych w bazie
        ordering = ('last_name', 'first_name')

        # po polsku w dopełniaczu
        verbose_name = _('author')

        verbose_name_plural = _('authors')


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return "{name}".format(name=self.name)


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'book categories'


class Book(models.Model):
    """
    Istniejąca książka, nie powiązana jeszcze z wydaniem, ani egzemplarzem
    """
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return "{title}".format(title=self.title)

    def get_authors(self):
        authors = self.authors.all()
        authors_str = ''

        for author in authors:
            authors_str = authors_str + ' ' + author.__str__()

        return authors_str.strip()

    def get_absolute_url(self):
        return reverse_lazy('shelf:book-detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ('title',)


class BookEdition(models.Model):
    """
    Wydanie książki istniejącej w bazie
    """
    book = models.ForeignKey(Book, related_name='editions')
    isbn = models.CharField(max_length=17)
    date = models.DateField()
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return "{book.title}, {publisher.name}" \
            .format(book=self.book, publisher=self.publisher)


COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard'),
)


class BookItem(models.Model):
    """
    Egzemplarz książki danego wydania
    """
    edition = models.ForeignKey(BookEdition)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    # get_cover_type_display() jest generowana dynamicznie dla pola z choices
    def __str__(self):
        return "{edition}, {cover} - {number}" \
            .format(edition=self.edition, cover=self.get_cover_type_display(),
                    number=self.catalogue_number)
