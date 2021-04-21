from django.shortcuts import render, redirect
from .models import Topic

# Create your views here.


def index(request):
    """The home page for learning_log"""
    return render(request, "MainApp/index.html")


def topics(request):
    topics = topic.objects.order_by(
        "data_added"
    )  # Order by = ascending or descending sort order

    context = {"topics": topics}
    return render(request, "MainApp/topics.html", context)
    # Context is an additional parameter passed to the index


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")  # The - puts it in desc order
    context = {"topic": topic, "entries": entries}

    return render(request, "MainApp/topic.html", context)

def new_topic(request):
    if request.method = 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=reuqest.POST) #takes info and adds to database

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')
    context = {'form':form}
    return render(request, 'MainApp/new_topic.html',context)
    # get request loads empty form
    # request.POST has all the info the user inputted on the website and adds to DB
    # is_valid() checks to make sure there's not errors on the form; if valid, save

