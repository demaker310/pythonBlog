from django.contrib.sitemaps import Sitemap
from .models import SubTopic, Topic


class SubTopicSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return SubTopic.objects.all()


class TopicSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Topic.objects.all()

