from django import template
from ..models import Topic


register = template.Library()


@register.inclusion_tag('_sidebar.html')
def all_topic():
    all_topics = Topic.objects.all()
    return {'all_topics': all_topics}
