from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """The home page for learning_log"""
    return render(request, "MainApp/index.html")


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")  # The - puts it in desc order
    context = {"topic": topic, "entries": entries}

    return render(request, "MainApp/topic.html", context)


def topics(request):
    topics = Topic.objects.order_by("date_added")
    # Order by = ascending or descending sort order

    context = {"topics": topics}
    return render(request, "MainApp/topics.html", context)
    # Context is an additional parameter passed to the index


def new_topic(request):
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)  # takes info and adds to database

        if form.is_valid():
            form.save()

            return redirect("MainApp:topics")
    context = {"form": form}
    return render(request, "MainApp/new_topic.html", context)
    # get request loads empty form
    # request.POST has all the info the user inputted on the website and adds to DB
    # is_valid() checks to make sure there's not errors on the form; if valid, save


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":  # load a new form
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            # with new entry, don't have associated topic
            new_entry.topic = topic
            new_entry.save()
            return redirect("MainApp:topic", topic_id=topic_id)
            #  Page 'Topic' requires id; so we pull the topic id from the first line to tell it where to go
    context = {"form": form, "topic": topic}
    # pass object "topic" instead of id so it will show the topic and pass all attributes
    return render(request, "MainApp/new_entry.html", context)
