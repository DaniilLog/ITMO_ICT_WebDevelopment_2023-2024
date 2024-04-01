```python
from datetime import timedelta

from django import template

register = template.Library()


@register.filter(name='format_duration')
def format_duration(value):
    if isinstance(value, timedelta):
        hours, remainder = divmod(value.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
    return value

```