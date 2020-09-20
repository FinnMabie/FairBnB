from django import template

register = template.Library()


@register.filter(name='is_auth')
def is_auth(user):
    if user.is_authenticated:
        return True
    else:
        return False
