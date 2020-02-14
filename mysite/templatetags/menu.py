from django import template
from book.models import Category

register = template.Library()


@register.inclusion_tag('common/left_menu.html')
def all_categorys(current_cid):
    """
    获取所有的分类
    :return:
    """
    categorys = Category.objects.all().order_by('-create_at')
    return {'categorys': categorys, 'current_cid' : current_cid}
