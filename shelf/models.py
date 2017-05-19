from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "{first_name} {last_name}" \
            .format(first_name=self.first_name, last_name=self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return "{name}".format(name=self.name)


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Istniejąca książka, nie powiązana jeszcze z wydaniem, ani egzemplarzem
    """
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return "{title}".format(title=self.title)


class BookEdition(models.Model):
    """
    Wydanie książki istniejącej w bazie
    """
    book = models.ForeignKey(Book)
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
        return "{edition}, {cover}" \
            .format(edition=self.edition, cover=self.get_cover_type_display())
