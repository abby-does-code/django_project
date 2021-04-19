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

    context= {'topics':topics}
    return render(request, "MainApp/topics.html",context)
    #Context is an additional parameter passed to the index
