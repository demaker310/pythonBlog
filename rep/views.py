from django.shortcuts import render, get_object_or_404
from .models import Topic, SubTopic
from django.contrib.postgres.search import TrigramSimilarity


def page_view(request, topic_slug=None, sub_topic_slug=None):
    if topic_slug and sub_topic_slug:
        page = get_object_or_404(SubTopic, slug=sub_topic_slug)
        all_pages = SubTopic.objects.all
        return render(request, f'rep/{page.topic.name}/{page.sub_topic}.html', {'page': page, 'all_pages': all_pages})
    elif topic_slug:
        topic = get_object_or_404(Topic, slug=topic_slug)
        all_topics = SubTopic.objects.all().filter(topic__slug=topic_slug)
        return render(request, 'rep/topic_view.html', {'topic': topic})
    else:
        return render(request, 'rep/index.html')


def process_search(request):
    search_str = ''
    results = []
    if request.method == 'POST':
        search_str = request.POST.get('search_str')
        if search_str:
            results = SubTopic.objects.annotate(
                similarity=TrigramSimilarity('description', search_str)
            ).filter(similarity__gt=0).order_by('-similarity')
            return render(request, 'search_results.html', {'search_string': search_str, 'results': results})
        else:
            search_str = request.POST.get('search-str-mobile')
            results = SubTopic.objects.annotate(
                similarity=TrigramSimilarity('description', search_str)
            ).filter(similarity__gt=0.1).order_by('-similarity')
            return render(request, 'search_results.html', {'search_string': search_str, 'results': results})
    else:
        return render(request, 'search_results.html', {'search_string': search_str, 'results': results})
