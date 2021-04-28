from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()  # log them in as we save their credentials
            login(request, new_user)
            return redirect("MainApp:index")

    context = {"form": form}  # Pass the template the form
    return render(request, "registration/register.html", context)


# All of this needsto be consistent! urls name needs to match view name and then our template name has to be the same_name.html
