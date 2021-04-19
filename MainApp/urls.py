from django.urls import path

from . import views

app_name = "MainApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("topics", views.topics, name="topics"),
]


# URL points to view and view is the brain behind gathering info and displaying
##Template as the bone and view as the neurons
