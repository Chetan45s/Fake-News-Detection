from django import template
register = template.Library()
import random

i = 0
a = [0,1,0,1,0]

@register.filter(name='define_ran')
def define_ran(ss):
    return random.choice([0,1,1])