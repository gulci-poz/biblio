from django.template import Library

register = Library()


@register.filter
def pub_date(date):
    return date.year


@register.inclusion_tag('tags/show_editions.html')
def show_editions(book):
    # kontekst dla szablonu
    return {'editions': book.editions.all()}


@register.inclusion_tag('tags/show_items.html')
def show_items(book):
    # alternatywne rozwiązanie:
    # można zaimportować BookItem
    # i zrobić zapytanie BookItem.objects.filter(edition__in=editions)
    items = []
    for edition in book.editions.all():
        for item in edition.bookitem_set.all():
            items.append(item)
    return {'items': items}
