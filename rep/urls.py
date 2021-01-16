from django.urls import path
from .views import page_view, process_search

app_name = 'pages'

urlpatterns = [
    path('', page_view, name='index'),
    path('search_results/', process_search, name='search'),
    path('<slug:topic_slug>/', page_view, name='page_view'),
    path('<slug:topic_slug>/<slug:sub_topic_slug>/', page_view, name='page_view'),
]
