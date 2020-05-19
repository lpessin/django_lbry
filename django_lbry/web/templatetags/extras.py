from datetime import datetime
from django import template


register = template.Library()


@register.filter("timestamp")
def timestamp(value):
    if isinstance(value, str):
        return 'Not found'
    else:        
        count = datetime.now() - datetime.fromtimestamp(value)
        count = count.days
        if count == 0:
            count = 'Today'
        else:
            count = f'{count} days ago'
        return count


