from django.template import Library

register = Library()


@register.filter
def pub_date(date):
    return date.year
