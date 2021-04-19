from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    """The home page for learning_log"""
    return render(request, "MainApp/index.html")


def topics(request):
    topics = Topic.objects.order_by(
        "data_added"
    )  # Order by = ascending or descending sort order

    context = {"topics": topics}
    return render(request, "MainApp/topics.html", context)
    # Context is an additional parameter passed to the index


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")  # The - puts it in desc order
    context = {'topic':topic,'entries':entries}
    
    return render(request, 'MainApp/topic.html',context)