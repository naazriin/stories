from django import template

register = template.Library()

from recipes.models import Category, Tags


@register.simple_tag
def get_categories(limit=5):
    cats = Category.objects.all()[:limit]
    return cats

@register.simple_tag
def get_tags(limit=5):
    tags = Tags.objects.all()[:limit]
    return tags


@register.filter
def upper(value):
    return value.upper()

@register.filter
def capitalize(value):
    return value.capitalize()


@register.filter
def custom_sentence_truncate(value):
    for i in value:
        if i == '.':
            return value[:value.index(i) + 1]