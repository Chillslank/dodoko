from django import template
from game.models import Category

register = template.Library()

@register.inclusion_tag('game/categories.html')
def get_category_list(current_catrgory=None):
    return {'categories':Category.objects.all(),
            'current_category':current_catrgory}