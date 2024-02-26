from django import template
from core.models import *

register = template.Library()

@register.filter
def display_entry_button(value, user):
    attended_today = Attendance.objects.filter(employee=user, entry__startswith=str(value)).first()
    if attended_today: 
        return False
    else:
        return True

@register.filter
def display_exit_button(value, user):
    attended_today = Attendance.objects.filter(employee=user, leave__startswith=str(value)).first()
    if attended_today: 
        return False
    else:
        return True
  
    # return False


@register.simple_tag
def value_1(value1,value2):
    return value1+""+value2