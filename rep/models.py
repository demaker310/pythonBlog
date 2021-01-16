from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=300, unique=True, help_text='You musn\'t use symbols', )
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=2000)
    meta_desc = models.TextField(max_length=1000)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Topic, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:page_view', args=[self.slug])

    def __str__(self):
        return self.name


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subtopics')
    sub_topic = models.CharField(max_length=200, help_text='You musn\'t use symbols')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=2000)
    meta_desc = models.TextField(max_length=1000)
    meta_keywords = models.CharField(max_length=1000)

    class Meta:
        ordering = ('-topic',)

    def save(self, *args, **kwargs):
        self.sub_topic = self.sub_topic.lower()
        return super(SubTopic, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:page_view', args=[self.topic.slug, self.slug])

    def __str__(self):
        return self.sub_topic

