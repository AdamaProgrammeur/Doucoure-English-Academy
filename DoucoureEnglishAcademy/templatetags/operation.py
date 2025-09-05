from django import template

register = template.Library()


@register.filter(name="addcent")
def addcent(value):
    return value + 1000

@register.filter(name="changeNom")
def changeNom(value):
    nouveau = value
    nouveau = "awa doucoure"
    return nouveau

@register.filter(name="cut")
def cut(value, arg):
    """Remove all values of arg from the given string"""
    return value.replace(arg, 'awa doucoure')
