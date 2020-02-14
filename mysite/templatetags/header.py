from django import template
from book.models import Category

register = template.Library()


@register.inclusion_tag('common/header.html')  #
def show_latest_categorys(count=3):
    latest_categorys = Category.objects.all().order_by('-create_at')[:count]
    return {'latest_categorys': latest_categorys, }


@register.simple_tag
def book_already_have(book):
    return book.amount - book.has_sell
