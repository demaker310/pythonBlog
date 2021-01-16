from django.contrib import admin
from .models import SubTopic, Topic


@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):
    fields = ['topic', 'sub_topic', 'slug', 'description', 'meta_desc', 'meta_keywords']
    search_fields = ['topic', 'sub_topic', 'description']
    list_display = ['topic', 'sub_topic', 'slug']
    raw_id_fields = ['topic']
    prepopulated_fields = {
        'slug': ('sub_topic',)}


@admin.register(Topic)
class Topic(admin.ModelAdmin):
    fields = ['name', 'slug', 'description', 'meta_desc', 'meta_keywords']
    list_display = ['name', 'description']
    prepopulated_fields = {
        'slug': ('name',)
    }

