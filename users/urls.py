from django.urls import path, include

app_name = "users"
urlpatterns = [path("", include("django.contrib.auth.urls"))]
# ^ using django's predesigned stuff for login
