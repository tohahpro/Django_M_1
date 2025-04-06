from django import template
from datetime import datetime
from django.utils import timezone

register  = template.Library()

# decorator 
@register.filter
def humanize_date(value):
    if value:
        today = datetime.now().date()
        value = timezone.localtime(value)
        if value.date() == today:
            return f"Today at {value.strftime("%I:%M %p")}"
        else:
            return value.strftime("%I:%M %p")
        
    return "No login record available"